from harc_rag.chunking.models import Chunk
from harc_rag.retrieval.fusion import ReciprocalRankFusion
from harc_rag.retrieval.models import RetrievalResult


def test_rrf():

    chunk = Chunk(
        chunk_id=1,
        text="TCP",
        start_index=0,
        end_index=3,
        metadata={},
    )

    dense = [
        RetrievalResult(
            chunk=chunk,
            score=0.9,
        )
    ]

    bm25 = [
        RetrievalResult(
            chunk=chunk,
            score=7.0,
        )
    ]

    fusion = ReciprocalRankFusion()

    results = fusion.fuse(
        dense,
        bm25,
    )

    assert len(results) == 1

    assert results[0].score > 0