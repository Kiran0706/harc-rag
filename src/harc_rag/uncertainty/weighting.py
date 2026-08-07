from dataclasses import dataclass


@dataclass
class ConfidenceWeights:

    retrieval: float

    generation: float

    evidence: float


class DynamicWeightCalculator:

    def calculate(
        self,
        retrieval_score: float,
    ) -> ConfidenceWeights:

        if retrieval_score >= 0.80:

            return ConfidenceWeights(
                retrieval=0.50,
                generation=0.20,
                evidence=0.30,
            )

        elif retrieval_score >= 0.60:

            return ConfidenceWeights(
                retrieval=0.45,
                generation=0.25,
                evidence=0.30,
            )

        else:

            return ConfidenceWeights(
                retrieval=0.60,
                generation=0.10,
                evidence=0.30,
            )