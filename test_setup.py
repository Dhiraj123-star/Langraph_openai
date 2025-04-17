import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

response = llm.invoke("Hello, are you working?")

print(response.content)