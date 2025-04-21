# 🧠 LangGraph OpenAI Agent API

A FastAPI application that uses **LangGraph**, **LangChain**, and **OpenAI's GPT-4o-mini** to perform intelligent NLP tasks on any input text. Just send a request and get structured insights instantly! ⚡

---

## 🚀 Features

- 📂 **Classification** — Detects whether your text is **News**, **Blog**, **Research**, or **Other**.
- 🧠 **Entity Extraction** — Pulls out **Person**, **Organization**, and **Location** entities.
- ✍️ **Summarization** — Generates a quick one-sentence summary.

---

## 🔌 Endpoint

**POST** `/analyze`

Send in a JSON with a `"text"` field, and get back:
- A classification category
- Extracted entities
- A concise summary

---

## 🛠️ Built With

- 🧩 LangGraph  
- 🦜 LangChain  
- 🤖 OpenAI GPT-4o-mini  
- ⚡ FastAPI  
- 🧪 Pydantic  
- 🔐 python-dotenv