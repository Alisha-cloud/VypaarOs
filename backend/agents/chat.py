from services.gemini import ask_gemini
from services.vector_store import (
    search_documents
)

def chat_agent(question):

    knowledge = search_documents(
        question
    )

    prompt = f"""
You are VyapaarOS AI Business Copilot.

Retrieved Business Knowledge:
{knowledge}

User Question:
{question}

Instructions:

- Use the retrieved business knowledge when answering.
- Give specific recommendations whenever possible.
- If a product is mentioned in the knowledge, reference it.
- Do not ask generic follow-up questions.
- Keep answers concise and actionable.
- If the knowledge is insufficient, clearly state that.

Answer:
"""

    return ask_gemini(prompt)