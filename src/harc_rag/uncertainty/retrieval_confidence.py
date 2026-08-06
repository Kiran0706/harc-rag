from harc_rag.retrieval.models import RetrievalResult


class RetrievalConfidenceEstimator:

    def estimate(
        self,
        results: list[RetrievalResult],
    ) -> float:

        if not results:
            return 0.0

        scores = [
            result.score
            for result in results
        ]

        confidence = sum(scores) / len(scores)

        confidence = max(
            0.0,
            min(confidence, 1.0),
        )

        return confidence