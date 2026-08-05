from rank_bm25 import BM25Okapi

from harc_rag.chunking.models import Chunk
from harc_rag.retrieval.models import RetrievalResult


class BM25Retriever:

    def __init__(self, chunks: list[Chunk]):

        self.chunks = chunks

        self.corpus = [
            chunk.text.split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(self.corpus)

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> list[RetrievalResult]:

        query_tokens = query.split()

        scores = self.bm25.get_scores(query_tokens)

        ranked = sorted(
            zip(self.chunks, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        results = []

        for chunk, score in ranked[:k]:

            results.append(
                RetrievalResult(
                    chunk=chunk,
                    score=float(score),
                )
            )

        return results