import os 
from groq import Groq
from dotenv import load_dotenv

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

if __name__ == "__main__":

    print("Testing the Model")

    test_prompt = "Explain what evidence means in an investigation in one sentence."
    response = test_groq_connection(test_prompt)

    print(response)