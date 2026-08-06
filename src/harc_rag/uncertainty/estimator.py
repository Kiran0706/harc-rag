from harc_rag.uncertainty.models import (
    ConfidenceScore,
    JointUncertainty,
)

from harc_rag.uncertainty.retrieval_confidence import (
    RetrievalConfidenceEstimator,
)


class JointEstimator:

    def __init__(self):

        self.retrieval = RetrievalConfidenceEstimator()

    def estimate(
        self,
        retrieval_results,
    ) -> JointUncertainty:

        retrieval_score = self.retrieval.estimate(
            retrieval_results
        )

        confidence = ConfidenceScore(
            retrieval=retrieval_score,
            generation=0.0,
            evidence=0.0,
        )

        return JointUncertainty(
            confidence=confidence,
            score=retrieval_score,
            should_verify=retrieval_score < 0.6,
        )