# Import necessary libraries
from dotenv import load_dotenv, find_dotenv
from google import genai
from google.genai import types
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())
# Get API key from environment variable
api_key = os.environ['GOOGLE_API_KEY'] 
client = genai.Client(api_key=api_key)
# Function to interact with Google's Gemini LLM
def llm(query: str) -> str:

    # 🔹 Step 1: Define the specialized prompt template
    prompt_template = """
    You are a knowledgeable and polite environmental expert who specializes only in Mangrove forests.  
    Your expertise includes their ecology, biodiversity, conservation, geography, environmental importance, and related scientific or social aspects.
    Do not provide greetings, like Hello!, Hi! in the response. Just jump straight to the context.
    If the user’s question is about Mangrove forests:
    - Provide a clear, detailed, and accurate explanation.
    - Use simple and structured language.
    If the user’s question is not about Mangrove forests:
    - Politely reply: "I’m sorry, but I can only answer questions related to Mangrove forests."
    If the user greets you (e.g., "Hi", "Hello"):
    - Respond warmly and politely, then mention that you can only answer questions related to Mangrove forests.
    Maintain a friendly, respectful, and informative tone at all times.

    User question:
    {query}
    """

    # Insert the user’s query into the prompt
    formatted_prompt = prompt_template.format(query=query)

    # 🔹 Step 2: Response handling with continuation mechanism
    full_text = ""
    continuation_prompt = formatted_prompt
    max_turns = 2  # safety limit to avoid infinite loops

    for _ in range(max_turns):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=[continuation_prompt],
                config=types.GenerateContentConfig(
                    max_output_tokens=900,
                    temperature=0.6,
                    top_p=0.9,
                    top_k=40,
                ),
            )

            text = ""
            if (
                hasattr(response, "candidates")
                and response.candidates
                and hasattr(response.candidates[0], "content")
                and response.candidates[0].content
                and response.candidates[0].content.parts
            ):
                text = response.candidates[0].content.parts[0].text
            else:
                return "No valid response received from the model."

            full_text += text

            finish_reason = response.candidates[0].finish_reason
            if finish_reason != "MAX_TOKENS":
                break

            continuation_prompt = f"Continue answering about Mangrove forests from where you left off:\n{text}"

        except Exception as e:
            if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
                return "The system is currently busy. Please try again after a few moments."
            else:
                return f"An error occurred: {e}"

    # Fallback return if loop never returns
    return full_text.strip() if full_text.strip() else "No response generated."


