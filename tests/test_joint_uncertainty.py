from harc_rag.chunking.models import Chunk
from harc_rag.retrieval.models import RetrievalResult
from harc_rag.uncertainty.estimator import JointEstimator


def test_joint_estimator():

    estimator = JointEstimator()

    retrieval = [

        RetrievalResult(

            chunk=Chunk(
                chunk_id=1,
                text="TCP handshake",
                start_index=0,
                end_index=12,
                metadata={},
            ),

            score=0.9,
        )
    ]

    result = estimator.estimate(

        retrieval_results=retrieval,

        answer="TCP handshake",

        context="TCP handshake protocol",

    )

    assert result.score > 0

    assert result.should_verify is False