class EvidenceConfidenceEstimator:

    def estimate(
        self,
        answer: str,
        context: str,
    ) -> float:

        if not answer.strip() or not context.strip():
            return 0.0

        answer_words = set(
            answer.lower().split()
        )

        context_words = set(
            context.lower().split()
        )

        overlap = answer_words.intersection(
            context_words
        )

        return len(overlap) / max(
            len(answer_words),
            1,
        )