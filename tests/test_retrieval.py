from harc_rag.retrieval.dense_retriever import DenseRetriever


def test_dense_retriever_creation():
    retriever = DenseRetriever(
        embedding_service=None,
        vector_store=None,
    )

    assert retriever.embedding_service is None
    assert retriever.vector_store is None