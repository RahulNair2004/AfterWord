import os 
from groq import Groq
from dotenv import load_dotenv
import json
from sqlalchemy.orm import Session
from app.services.AI.context import build_case_ai_context, build_evidence_ai_context
from app.services.AI.prompts import CASE_SUMMARY_SYSTEM_PROMPT, EVIDENCE_ANALYSIS_SYSTEM_PROMPT
from app.services.AI.schemas import CaseSummaryResponse, EvidenceAnalysisResponse
from app.db.database import get_db

# Load variables from .env files

load_dotenv()

# Loading the environment parameters
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is missing.")

# Initialize a Groq Client
client = Groq(api_key = GROQ_API_KEY)

# Create our single test function 
def test_groq_connection(prompt: str) -> str:

    # Send only plain text prompt and extract only model text response

    try:
        completion = client.chat.completions.create(
            model = GROQ_MODEL,
            messages  = [
                {
                    "role":"system",
                    "content":"You are a precise criminal investigation assistant for a game called AfterWords."
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            temperature = 0.2,
        )

        # Extract and return only text content string
        return completion.choices[0].message.content

    except Exception as e:
        return f"Groq Connection Error: {str(e)}"

def generate_case_summary(case_id: int,db:Session) -> CaseSummaryResponse:

    # Fetch text profile from context layer
    case_context = build_case_ai_context(case_id=case_id,db=db)

    # Check if the case profile context exists
    if not case_context:
        raise ValueError(f"Case with ID {case_id} was not found.")

    # Formulating the explicit role instruction
    completion = client.chat.completions.create(
        model = GROQ_MODEL,
        messages = [
            {
                "role":"system",
                "content":CASE_SUMMARY_SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":case_context
            }
        ],
        temperature = 0.2,

        response_format = {"type":"json_object"}
    )


    # Extract JSON payload string response
    json_string = completion.choices[0].message.content

    # parsed data
    parsed_data = json.loads(json_string)

    # Push data dictionary onto pydantic validator model
    validated_response = CaseSummaryResponse(**parsed_data)

    return validated_response

def generate_evidence_analysis(evidence_id: int, db: Session) -> EvidenceAnalysisResponse:

    # Calling the context builder for evidence analysis
    evidence_context = build_evidence_ai_context(evidence_id=evidence_id, db=db)

    # Stop if context layer has empty srtings
    if not evidence_context:
        raise ValueError(f"Evidence with ID {evidence_id} was not found.")

    # The LLM chat completion call
    completion = client.chat.completions.create(
        model = GROQ_MODEL,
        messages = [
            {"role": "system", "content": EVIDENCE_ANALYSIS_SYSTEM_PROMPT},
            {"role": "user", "content": evidence_context}
        ],
        temperature = 0.2,
        response_format = {"type":"json_object"}
    )

    # Extracting the JSON payload response
    json_string = completion.choices[0].message.content

    # Parsing the JSON string 
    parsed_data = json.loads(json_string)

    # Validating the parsed data 
    validated_response  = EvidenceAnalysisResponse(**parsed_data)

    return validated_response
    
if __name__ == "__main__":

    print("Connecting to Postgresql")
    db_generator = get_db()
    db = next(db_generator)

    TARGET_EVIDENCE_ID = 1

    try:
        ai_response = generate_evidence_analysis(evidence_id=TARGET_EVIDENCE_ID, db=db)

        print(ai_response.summary)
        
        print(ai_response.significance)
        
        for connection in ai_response.possible_connections:
            print(f"• {connection}")
            
        for question in ai_response.questions:
            print(f"• {question}")
            
    
    except ValueError as ve:
        print(f"\n Validation Error: {str(ve)}")

    except Exception as e:
        print(f"\nPipeline Crash Trace: {str(e)}")
    
    finally:
        # Clean up the database hook properly
        try:
            next(db_generator)
        except StopIteration:
            pass
    