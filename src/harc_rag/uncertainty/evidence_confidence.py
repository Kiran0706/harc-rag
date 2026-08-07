from harc_rag.uncertainty.semantic_similarity import (
    SemanticSimilarity,
)


class EvidenceConfidenceEstimator:

    def __init__(self):

        self.semantic = SemanticSimilarity()

    def estimate(
        self,
        answer: str,
        context: str,
    ) -> float:

        return self.semantic.similarity(
            answer,
            context,
        )