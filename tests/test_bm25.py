from harc_rag.chunking.models import Chunk
from harc_rag.retrieval.bm25_retriever import BM25Retriever


def test_bm25():

    chunks = [
        Chunk(
            chunk_id=0,
            text="TCP uses a three-way handshake.",
            start_index=0,
            end_index=30,
            metadata={},
        ),
        Chunk(
            chunk_id=1,
            text="UDP is connectionless.",
            start_index=31,
            end_index=55,
            metadata={},
        ),
    ]

    retriever = BM25Retriever(chunks)

    results = retriever.retrieve("TCP")

    assert len(results) == 2
    assert "TCP" in results[0].chunk.text