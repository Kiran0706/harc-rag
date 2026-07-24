from harc_rag.retrieval.config import RetrievalConfig
from harc_rag.retrieval.service import RetrievalService


class FakeRetriever:

    def retrieve(self, query, k):
        return []


def test_retrieval_service():

    service = RetrievalService(
        retriever=FakeRetriever(),
        config=RetrievalConfig(top_k=3),
    )

    results = service.retrieve("What is TCP?")

    assert results == []