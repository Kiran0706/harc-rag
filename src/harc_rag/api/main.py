from fastapi import FastAPI

from harc_rag.api.routes import router, set_pipeline
from harc_rag.pipeline.pipeline import HARCRAGPipeline


app = FastAPI(
    title="HARC-RAG API",
    description="Hallucination-Aware Retrieval-Augmented Generation API",
    version="0.1.0",
)


# Create your existing retriever here.
#
# Example:
#
# retriever = YourExistingRetriever(...)
#
# pipeline = HARCRAGPipeline(retriever)
# set_pipeline(pipeline)


app.include_router(router)


@app.get("/")
def root():

    return {
        "message": "HARC-RAG API is running"
    }