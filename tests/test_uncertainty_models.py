from harc_rag.uncertainty.models import (
    ConfidenceScore,
    JointUncertainty,
)


def test_uncertainty_models():

    confidence = ConfidenceScore(
        retrieval=0.8,
        generation=0.9,
        evidence=0.7,
    )

    result = JointUncertainty(
        confidence=confidence,
        score=0.8,
        should_verify=False,
    )

    assert result.score == 0.8
    assert result.confidence.retrieval == 0.8