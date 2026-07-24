from harc_rag.retrieval.config import RetrievalConfig


class RetrievalService:

    def __init__(
        self,
        retriever,
        config: RetrievalConfig,
    ):
        self.retriever = retriever
        self.config = config

    def retrieve(self, query: str):
        return self.retriever.retrieve(
            query=query,
            k=self.config.top_k,
        )