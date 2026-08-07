class CostEstimator:

    def estimate(
        self,
        answer: str,
        context: str,
    ) -> float:

        answer_words = len(answer.split())

        context_words = len(context.split())

        cost = (
            answer_words * 0.4
            + context_words * 0.6
        )

        return cost