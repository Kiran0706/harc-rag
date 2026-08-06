from harc_rag.uncertainty.models import (
    ConfidenceScore,
    JointUncertainty,
)

from harc_rag.uncertainty.retrieval_confidence import (
    RetrievalConfidenceEstimator,
)

from harc_rag.uncertainty.generation_confidence import (
    GenerationConfidenceEstimator,
)

from harc_rag.uncertainty.evidence_confidence import (
    EvidenceConfidenceEstimator,
)


class JointEstimator:

    def __init__(self):

        self.retrieval = RetrievalConfidenceEstimator()
        self.generation = GenerationConfidenceEstimator()
        self.evidence = EvidenceConfidenceEstimator()

    def estimate(
        self,
        retrieval_results,
        answer,
        context,
    ) -> JointUncertainty:

        retrieval = self.retrieval.estimate(
            retrieval_results
        )

        generation = self.generation.estimate(
            answer
        )

        evidence = self.evidence.estimate(
            answer,
            context,
        )

        joint = (
            0.40 * retrieval
            + 0.30 * generation
            + 0.30 * evidence
        )

        confidence = ConfidenceScore(
            retrieval=retrieval,
            generation=generation,
            evidence=evidence,
        )

        return JointUncertainty(
            confidence=confidence,
            score=joint,
            should_verify=joint < 0.65,
        )