# Import necessary libraries
from dotenv import load_dotenv, find_dotenv
from google import genai
from google.genai import types
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())
# Get API key from environment variable
api_key = os.environ['GOOGLE_API_KEY'] 

# Function to query LangChain Language Model (LLM)
def query_llm(query, vector_store):
    # Use document similarity search to find relevant passages
    docs = vector_store.similarity_search(query, k=3)
    relevant = "\n\n".join([doc.page_content for doc in docs])

    # Template for generating a structured input for the LLM
    template = f"""
    You are a knowledgeable and friendly environmental assistant who specializes exclusively in Mangrove forests. 
    Use only the information from the passage below to answer the user's question.
    Do not provide greetings, like Hello!, Hi! in the response. Just jump straight to the context.
    If the user greets you (e.g., "Hi", "Hello"):
    - Respond warmly and politely, then mention that you can only answer questions related to Mangrove forests and from the document that the user has uploaded.
    Maintain a friendly, respectful, and informative tone at all times.

    Your task:
    - Provide clear, detailed, and comprehensive answers in 200–300 words.
    - Keep the tone conversational and easy for a non-technical audience to understand.
    - Include relevant background details when necessary.
    - Do not provide affirmations like "Sure!" or "Let's explore this!" — give only the direct, relevant answer.
    - Answer strictly using the provided passage about Mangrove forests.
    - If the question is not related to Mangrove forests or the answer is not found in the passage, reply with:
    "I’m sorry, but I can only answer questions related to Mangrove forests. Either the question seems to be irrelevant or the uploaded document doesn't have sufficient information on this topic."

    QUESTION: '{query}'
    PASSAGE: '{relevant}'

    ANSWER:
    """
    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[template],
            config=types.GenerateContentConfig(
            max_output_tokens=500,
            temperature=0.6,
            top_p=0.9,
            top_k=40
            # stop_sequences=['\n']
        )
        )
        return response.text
    
    except Exception as e:
        if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
            return "The system is currently busy. Please try again after a few moments."
        else:
            return f"An error occurred: {e}"
