from fastapi import FastAPI

from workflow.graph import workflow
from schemas.request import GoalRequest

app = FastAPI(
    title="VyapaarOS",
    description="Autonomous Business Intelligence Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "VyapaarOS Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze(request: GoalRequest):

    result = workflow.invoke(
        {
            "goal": request.goal
        }
    )

    return result