import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:latest"

def finance_advice(query):

    prompt = f"""
You are an AI Finance Assistant.

User Question:
{query}

Provide:
1. Financial Advice
2. Budget Tips
3. Saving Suggestions

Keep the answer simple and short.

Do not give investment or legal advice.
"""

    try:

        response = requests.post(

            OLLAMA_URL,

            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }

        )

        return response.json()["response"]

    except:

        return "Unable to connect to Ollama."