class AdaptiveThreshold:

    def calculate(
        self,
        question: str,
    ) -> float:

        words = len(question.split())

        if words <= 5:
            return 0.80

        elif words <= 12:
            return 0.70

        return 0.60