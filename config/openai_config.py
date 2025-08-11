import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm(temperature=0.5):
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature= temperature,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )