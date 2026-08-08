from fastapi import APIRouter, HTTPException

from harc_rag.api.models import ChatRequest, ChatResponse


router = APIRouter()

_pipeline = None


def set_pipeline(pipeline):
    global _pipeline
    _pipeline = pipeline


@router.get("/health")
def health():

    return {
        "status": "ok"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    if _pipeline is None:

        raise HTTPException(
            status_code=503,
            detail="HARC-RAG pipeline is not initialized",
        )

    answer = _pipeline.answer(
        request.question
    )

    return ChatResponse(
        answer=answer
    )