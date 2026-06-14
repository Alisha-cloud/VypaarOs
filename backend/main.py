from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from workflow.graph import workflow
from schemas.request import GoalRequest


app = FastAPI(
    title="VyapaarOS",
    description="Autonomous Business Intelligence Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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