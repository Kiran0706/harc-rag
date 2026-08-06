class GenerationConfidenceEstimator:

    UNCERTAIN_PHRASES = [
        "i don't know",
        "not sure",
        "possibly",
        "maybe",
        "might",
        "could be",
        "cannot determine",
        "insufficient information",
    ]

    def estimate(
        self,
        answer: str,
    ) -> float:

        if not answer.strip():
            return 0.0

        answer_lower = answer.lower()

        confidence = 1.0

        for phrase in self.UNCERTAIN_PHRASES:

            if phrase in answer_lower:
                confidence -= 0.15

        confidence = max(
            0.0,
            min(confidence, 1.0),
        )

        return confidence