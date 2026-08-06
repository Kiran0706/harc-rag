import pytest
from harc_rag.chunking.models import Chunk
from harc_rag.retrieval.models import RetrievalResult
from harc_rag.uncertainty.retrieval_confidence import (
    RetrievalConfidenceEstimator,
)


def test_retrieval_confidence():

    estimator = RetrievalConfidenceEstimator()

    results = [

        RetrievalResult(
            chunk=Chunk(
                chunk_id=1,
                text="TCP",
                start_index=0,
                end_index=3,
                metadata={},
            ),
            score=0.9,
        ),

        RetrievalResult(
            chunk=Chunk(
                chunk_id=2,
                text="Handshake",
                start_index=4,
                end_index=12,
                metadata={},
            ),
            score=0.8,
        ),
    ]

    confidence = estimator.estimate(results)

    assert confidence == pytest.approx(0.85)