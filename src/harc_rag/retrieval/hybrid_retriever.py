from harc_rag.retrieval.interfaces import Retriever
from harc_rag.retrieval.models import RetrievalResult
from harc_rag.retrieval.bm25_retriever import BM25Retriever


class HybridRetriever(Retriever):

    def __init__(
        self,
        dense_retriever: Retriever,
        bm25_retriever: BM25Retriever,
    ):
        self.dense_retriever = dense_retriever
        self.bm25_retriever = bm25_retriever

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> list[RetrievalResult]:

        dense_results = self.dense_retriever.retrieve(query, k)

        bm25_results = self.bm25_retriever.retrieve(query, k)

        merged = {}

        for result in dense_results:
            merged[result.chunk.chunk_id] = result

        for result in bm25_results:

            if result.chunk.chunk_id in merged:

                merged[result.chunk.chunk_id].score += result.score

            else:

                merged[result.chunk.chunk_id] = result

        results = sorted(
            merged.values(),
            key=lambda x: x.score,
            reverse=True,
        )

        return results[:k]