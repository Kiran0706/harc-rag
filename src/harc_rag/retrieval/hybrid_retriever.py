from harc_rag.retrieval.interfaces import Retriever
from harc_rag.retrieval.models import RetrievalResult
from harc_rag.retrieval.bm25_retriever import BM25Retriever
from harc_rag.retrieval.fusion import ReciprocalRankFusion


class HybridRetriever(Retriever):

    def __init__(
        self,
        dense_retriever: Retriever,
        bm25_retriever: BM25Retriever,
    ):

        self.dense_retriever = dense_retriever

        self.bm25_retriever = bm25_retriever

        self.fusion = ReciprocalRankFusion()

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> list[RetrievalResult]:

        dense = self.dense_retriever.retrieve(query, k)

        bm25 = self.bm25_retriever.retrieve(query, k)

        return self.fusion.fuse(
            dense,
            bm25,
        )[:k]