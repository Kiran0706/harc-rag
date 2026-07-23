from harc_rag.vectorstore.faiss_store import FAISSVectorStore


def test_create_store():
    store = FAISSVectorStore()

    assert store.index is None
    assert store.embeddings == []