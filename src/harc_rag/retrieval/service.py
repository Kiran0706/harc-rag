from harc_rag.retrieval.dense_retriever import DenseRetriever


class RetrievalService:

    def __init__(self, retriever: DenseRetriever):
        self.retriever = retriever

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ):
        return self.retriever.retrieve(query, k)