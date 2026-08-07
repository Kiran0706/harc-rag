from harc_rag.routing.models import RoutingDecision
from harc_rag.uncertainty.threshold import AdaptiveThreshold


class AdaptiveRouter:

    def __init__(self):
        self.threshold = AdaptiveThreshold()

    def route(
        self,
        confidence: float,
        question: str,
    ):

        threshold = self.threshold.calculate(question)

        if confidence < threshold:

            return RoutingDecision(
                should_verify=True,
                confidence=confidence,
                reason=f"Below threshold ({threshold:.2f})",
            )

        return RoutingDecision(
            should_verify=False,
            confidence=confidence,
            reason=f"Above threshold ({threshold:.2f})",
        )