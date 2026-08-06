import pytest
from harc_rag.uncertainty.generation_confidence import (
    GenerationConfidenceEstimator,
)


def test_generation_confidence():

    estimator = GenerationConfidenceEstimator()

    confidence = estimator.estimate(
        "TCP uses a three-way handshake."
    )

    assert confidence == 1.0


def test_uncertain_generation():

    estimator = GenerationConfidenceEstimator()

    confidence = estimator.estimate(
        "Maybe TCP uses a handshake."
    )

    assert confidence < 1.0