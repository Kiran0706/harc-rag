from harc_rag.embedding.models import Embedding
from harc_rag.vectorstore.faiss_store import FAISSVectorStore


def test_faiss():

    store = FAISSVectorStore()

    embeddings = [
        Embedding(
            chunk_id=0,
            vector=[1.0, 0.0, 0.0],
        ),
        Embedding(
            chunk_id=1,
            vector=[0.0, 1.0, 0.0],
        ),
        Embedding(
            chunk_id=2,
            vector=[0.0, 0.0, 1.0],
        ),
    ]

    store.add(embeddings)

    results = store.search(
        [1.0, 0.0, 0.0],
        k=2,
    )

    assert len(results) == 2

    assert results[0].embedding.chunk_id == 0