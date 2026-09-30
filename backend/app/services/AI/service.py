import os 
from groq import Groq
from dotenv import load_dotenv
import json
from sqlalchemy.orm import Session
from app.services.AI.context import build_case_ai_context
from app.services.AI.prompts import CASE_SUMMARY_SYSTEM_PROMPT
from app.services.AI.schemas import CaseSummaryResponse

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

def generate_case_summary(case_id: int,db:Session):

    # Fetch text profile from context layer
    case_context = build_case_ai_context(case_id=case_id,db=db)

    # Check if the case profile context exists
    if case_context:
        raise ValueError(f"Case with ID {case_id} was not found.")

    # Formulating the explicit role instruction
    completion = client.chat.completion.create(
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
        temperature = 0.3,

        response_format = {"type":"json_object"}
    )


    # Extract JSON payload string response

    json_string = completion.choices[0].message.content

    # parsed data
    parsed_data = json.load(json_string)

    # Push data dictionary onto pydantic validator model
    validated_response = CaseSummaryResponse(**parsed_data)

    return validated_response

if __name__ == "__main__":

    print("Testing the Model")

    test_prompt = "Explain what evidence means in an investigation in one sentence."
    response = test_groq_connection(test_prompt)

    print(response)