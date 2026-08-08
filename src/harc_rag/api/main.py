from pydantic import BaseModel
from fastapi import FastAPI

from harc_rag.api.routes import router

class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str



app = FastAPI(
    title="HARC-RAG API",
    description="Hallucination-Aware Retrieval-Augmented Generation API",
    version="0.1.0",
)


app.include_router(router)


@app.get("/")
def root():

    return {
        "message": "HARC-RAG API is running"
    }