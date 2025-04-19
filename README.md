🧠 Text Intelligence API with LangGraph + OpenAI
This project provides a simple API that performs automated text analysis using a LangGraph workflow powered by OpenAI's GPT models.

🚀 Functionality
Text Classification
Classifies the input text as one of: News, Blog, Research, or Other.

Entity Extraction
Extracts named entities such as Person, Organization, and Location.

Text Summarization
Generates a short one-sentence summary of the input text.

📮 API Endpoint
POST /analyze
Request Body:

json
Copy
Edit
{
  "text": "Your input text goes here."
}
Response:

json
Copy
Edit
{
  "classification": "Research",
  "entities": ["John Doe", "OpenAI", "San Francisco"],
  "summary": "This text provides insights into research conducted by OpenAI."
}
🐳 Docker
You can build and run the app using Docker:

bash
Copy
Edit
docker build -t your-image-name .
docker run -p 8000:8000 your-image-name
Or with Docker Compose (pulls latest image automatically):

bash
Copy
Edit
docker-compose up -d
⚙️ CI/CD with GitHub Actions
Every push to the main branch automatically:

Builds the Docker image

Pushes it to Docker Hub

Keeps your deployment up to date