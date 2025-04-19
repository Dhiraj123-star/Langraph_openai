import os
from typing import TypedDict, List
from fastapi import FastAPI
from pydantic import BaseModel
from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

"""
LangGraph OpenAI Agent API 🚀

This FastAPI application integrates with LangGraph and OpenAI's GPT-4o-mini model 
to perform three key NLP tasks on any input text:

1. 📂 Classification - Categorizes text into News, Blog, Research, or Other.
2. 🧠 Entity Extraction - Extracts entities like Person, Organization, and Location.
3. ✍️ Summarization - Generates a short one-sentence summary of the input.

Endpoint:
POST /analyze
Request Body: { "text": "<your input text>" }
Response: { "classification": "...", "entities": [...], "summary": "..." }

Powered by LangGraph + LangChain + FastAPI.
"""


# Set up LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Define Agent State
class State(TypedDict):
    text: str
    classification: str
    entities: List[str]
    summary: str

# Define API input model
class TextRequest(BaseModel):
    text: str

# Define nodes
def classification_node(state: State):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Classify the following text into one of the categories: News, Blog, Research, or Other.\n\nText: {text}\n\nCategory:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    classification = llm.invoke([message]).content.strip()
    return {"classification": classification}

def entity_extraction_node(state: State):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Extract all the entities (Person, Organization, Location) from the following text. Provide the result as a comma-separated list.\n\nText: {text}\n\nEntities:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    entities = llm.invoke([message]).content.strip().split(", ")
    return {"entities": entities}

def summarize_node(state: State):
    summarization_prompt = PromptTemplate.from_template(
        "Summarize the following text in one short sentence.\n\nText: {text}\n\nSummary:"
    )
    chain = summarization_prompt | llm
    response = chain.invoke({"text": state["text"]})
    return {"summary": response.content}

# Build LangGraph workflow
workflow = StateGraph(State)
workflow.add_node("classification_node", classification_node)
workflow.add_node("entity_extraction", entity_extraction_node)
workflow.add_node("summarization", summarize_node)

workflow.set_entry_point("classification_node")
workflow.add_edge("classification_node", "entity_extraction")
workflow.add_edge("entity_extraction", "summarization")
workflow.add_edge("summarization", END)

app_graph = workflow.compile()

# FastAPI App
app = FastAPI(
    title="🧠 LangGraph OpenAI Agent API",
    description="""
LangGraph OpenAI Agent API 🚀

This FastAPI application uses LangGraph and OpenAI's GPT-4o-mini model 
to perform intelligent NLP tasks on input text:

### Features:
- 📂 **Classification** - Categorizes text into News, Blog, Research, or Other.
- 🧠 **Entity Extraction** - Extracts Person, Organization, and Location entities.
- ✍️ **Summarization** - Produces a concise summary of the input.
"""
)

@app.post("/analyze")
def analyze_text(request: TextRequest):
    result = app_graph.invoke({"text": request.text})
    return {
        "classification": result["classification"],
        "entities": result["entities"],
        "summary": result["summary"]
    }
