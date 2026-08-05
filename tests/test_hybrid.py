from harc_rag.chunking.models import Chunk
from harc_rag.retrieval.hybrid_retriever import HybridRetriever
from harc_rag.retrieval.models import RetrievalResult


class FakeDenseRetriever:

    def retrieve(self, query, k=5):

        return [
            RetrievalResult(
                chunk=Chunk(
                    chunk_id=1,
                    text="TCP",
                    start_index=0,
                    end_index=3,
                    metadata={},
                ),
                score=0.9,
            )
        ]


class FakeBM25Retriever:

    def retrieve(self, query, k=5):

        return [
            RetrievalResult(
                chunk=Chunk(
                    chunk_id=1,
                    text="TCP",
                    start_index=0,
                    end_index=3,
                    metadata={},
                ),
                score=5.2,
            )
        ]


def test_hybrid():

    retriever = HybridRetriever(
        FakeDenseRetriever(),
        FakeBM25Retriever(),
    )

    results = retriever.retrieve("TCP")

    assert len(results) == 1

    assert results[0].score > 0