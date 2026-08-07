from harc_rag.uncertainty.weighting import (
    DynamicWeightCalculator,
)


def test_high_retrieval():

    calculator = DynamicWeightCalculator()

    weights = calculator.calculate(0.90)

    assert weights.retrieval == 0.50

    assert weights.generation == 0.20

    assert weights.evidence == 0.30


def test_low_retrieval():

    calculator = DynamicWeightCalculator()

    weights = calculator.calculate(0.40)

    assert weights.retrieval == 0.60

    assert weights.generation == 0.10

    assert weights.evidence == 0.30