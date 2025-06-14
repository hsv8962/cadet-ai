from langchain_community.llms import Ollama
from dotenv import load_dotenv
from .model_settings import DEFAULT_MODEL, MODEL_SOURCE

def get_chatbot_response(user_input: str) -> str:
    return llm.invoke(user_input)

load_dotenv()

llm = Ollama(model="llama3")

def get_chatbot_response(user_input: str) -> str:
    return llm.invoke(user_input)

