import os 
from groq import Groq
from dotenv import load_dotenv
import json
from sqlalchemy.orm import Session
from app.services.AI.context import build_case_ai_context, build_evidence_ai_context, build_theory_ai_context, build_investigation_assistant_context, build_paradox_ai_context
from app.services.AI.prompts import CASE_SUMMARY_SYSTEM_PROMPT, EVIDENCE_ANALYSIS_SYSTEM_PROMPT, THEORY_ANALYSIS_SYSTEM_PROMPT, INVESTIGATION_ASSISTANT_SYSTEM_PROMPT, PARADOX_AI_SYSTEM_PROMPT
from app.services.AI.schemas import CaseSummaryResponse, EvidenceAnalysisResponse, TheoryAnalysisResponse, InvestigationAssistantResponse, InvestigationAssistantRequest, ParadoxMessage, ParadoxAIResponse
from app.models.ai import AIAnalysis
from app.db.database import get_db
from app.models.evidence import Evidence
from app.models.theory import Theory

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

    cached_summary = (
    db.query(AIAnalysis)
    .filter(
        AIAnalysis.case_id == case_id,
        AIAnalysis.analysis_type == "case_summary"
    )
    .first()
)

    if cached_summary:
        return CaseSummaryResponse(**cached_summary.response)

       
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

    # Cache Insertion Phase
    new_analysis = AIAnalysis(
        case_id = case_id,
        evidence_id=None,
        theory_id=None,
        analysis_type="case_summary",
        response=validated_response.model_dump(),
        model=GROQ_MODEL
    )

    db.add(new_analysis)

    db.commit()

    db.refresh(new_analysis)

    return validated_response

def generate_evidence_analysis(evidence_id: int, db: Session) -> EvidenceAnalysisResponse:

    evidence = (
        db.query(Evidence)
        .filter(Evidence.id == evidence_id)
        .first()
    )

    if not evidence:
        raise ValueError(f"Evidence with ID {evidence_id} was not found.")

    
    # Calling the context builder for evidence analysis
    evidence_context = build_evidence_ai_context(evidence_id=evidence_id, db=db)

    # Stop if context layer has empty srtings
    if not evidence_context:
        raise ValueError(f"Evidence with ID {evidence_id} was not found.")

    cached_analysis = (
        db.query(AIAnalysis)
        .filter(
            AIAnalysis.evidence_id == evidence_id,
            AIAnalysis.analysis_type == "evidence_analysis"
        )
        .first()
    )

    if cached_analysis:
        return EvidenceAnalysisResponse(**cached_analysis.response)

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
    print("CACHE HIT - RETURNING SAVED Evidence ANALYSIS")
    validated_response  = EvidenceAnalysisResponse(**parsed_data)

    new_analysis = AIAnalysis(
        case_id=evidence.case_id,
        evidence_id=evidence_id,
        theory_id=None,
        analysis_type="evidence_analysis",
        response=validated_response.model_dump(),
        model=GROQ_MODEL
    )

    db.add(new_analysis)
    db.commit()
    db.refresh(new_analysis)
 
    return validated_response

def generate_theory_analysis(theory_id: int, db: Session) -> TheoryAnalysisResponse:

    # Fetching theory from the db
    theory = (
        db.query(Theory)
        .filter(Theory.id == theory_id)
        .first()
    )
    # if empty raise error
    if not theory:
        raise ValueError(f"Theory with ID {theory_id} was not found.")

    # Calling the context builder for theory analysis
    theory_context = build_theory_ai_context(theory_id = theory_id, db = db)

    # Stop if context layer has empty strings
    if not theory_context:
        raise ValueError(f"Theory with ID {theory_id} was not found.")

    # Cache integration
    cached_analysis = (
        db.query(AIAnalysis)
        .filter(
            AIAnalysis.theory_id == theory_id,
            AIAnalysis.analysis_type == "theory_analysis"
        )
        .first()
    )

    # If cache exists return same response
    if cached_analysis:
        return TheoryAnalysisResponse(**cached_analysis.response)

    
    # LLM chat ccompletion call
    completion = client.chat.completions.create(
        model = GROQ_MODEL,
        messages = [
            {"role":"system","content":THEORY_ANALYSIS_SYSTEM_PROMPT},
            {"role":"user","content":theory_context}
        ],
        temperature = 0.2,
        response_format = {"type":"json_object"}
    )

    # Extracting the JSON payload response
    json_string  = completion.choices[0].message.content

    # Parsing the JSON string
    parsed_string = json.loads(json_string)

    # Validating the parsed string
    print("CACHE HIT - RETURNING SAVED THEORY ANALYSIS")
    validated_response = TheoryAnalysisResponse(**parsed_string)

    # Instantiate new analysis for theory 
    new_analysis = AIAnalysis(
        case_id=theory.case_id,
        evidence_id=None,
        theory_id=theory_id,
        analysis_type="theory_analysis",
        response=validated_response.model_dump(),
        model=GROQ_MODEL
    )

    # Add the new instiated analyses into the db
    db.add(new_analysis)
    db.commit()
    db.refresh(new_analysis)

    return validated_response

def generate_investigation_assistant(case_id: int, question: str, db: Session) -> InvestigationAssistantResponse:

    # Calling context builder
    investigation_context = build_investigation_assistant_context(case_id=case_id, db=db)

    # Stop if empty
    if not investigation_context:
        raise ValueError(f"Case with ID {case_id} not found.")

    

    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
        {"role": "system", "content": INVESTIGATION_ASSISTANT_SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                f"Case context:\n{investigation_context}\n\n"
                f"Investigator question:\n{question}"
            )
        }
    ],
        temperature=0.2,
        response_format={"type": "json_object"}
    )

    json_string = completion.choices[0].message.content
    parsed_data = json.loads(json_string)
    validated_response = InvestigationAssistantResponse(**parsed_data)

    return validated_response

def generate_paradox_ai(case_id: int,messages: list[ParadoxMessage],db: Session) -> ParadoxAIResponse:

    # Calling the context builder
    paradox_context = build_paradox_ai_context(case_id = case_id, messages = messages,db= db)

    # If empty Stop
    if not paradox_context:
        raise ValueError(f"Case with ID {case_id} not found.")    

    completion = client.chat.completions.create(
        model = GROQ_MODEL,
        messages = [
            {"role":"system","content":PARADOX_AI_SYSTEM_PROMPT},
            {"role":"user","content":paradox_context}
        ],
        temperature =0.2,
        response_format = {"type":"json_object"}
    )

    # Extracting the JSON payload response
    json_string = completion.choices[0].message.content

    # Parsing the JSON string
    parsed_data = json.loads(json_string)

    # Validating the parsed string 
    validated_response = ParadoxAIResponse(**parsed_data)
    return validated_response


if __name__ == "__main__":
    print("Connecting to Postgresql")

    db_generator = get_db()
    db = next(db_generator)

    TARGET_CASE_ID = 1

    messages = [
        ParadoxMessage(
            role="user",
            content="The thief definitely entered through the broken window."
        ),
        ParadoxMessage(
            role="assistant",
            content=(
                "The broken window may support that possibility, "
                "but the available evidence does not establish that it was the entry point."
            )
        ),
        ParadoxMessage(
            role="user",
            content="But the room was locked, so the window must have been used."
        )
    ]

    try:
        ai_response = generate_paradox_ai(
            case_id=TARGET_CASE_ID,
            messages=messages,
            db=db
        )

        print("\nCHALLENGE:")
        print(ai_response.challenge)

        print("\nALTERNATIVE EXPLANATIONS:")
        for explanation in ai_response.alternative_explanations:
            print(f"• {explanation}")

        print("\nSUPPORTING POINTS:")
        for point in ai_response.supporting_points:
            print(f"• {point}")

        print("\nCOUNTER QUESTIONS:")
        for question in ai_response.counter_questions:
            print(f"• {question}")

    except ValueError as ve:
        print(f"\nValidation Error: {str(ve)}")

    except Exception as e:
        print(f"\nPipeline Crash Trace: {str(e)}")

    finally:
        try:
            next(db_generator)
        except StopIteration:
            pass