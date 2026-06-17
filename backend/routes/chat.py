from fastapi import APIRouter

from agents.chat import (
    chat_agent
)

router = APIRouter()


@router.post("/chat")
def chat(data: dict):

    answer = chat_agent(
        data["question"]
    )

    return {
        "answer": answer
    }