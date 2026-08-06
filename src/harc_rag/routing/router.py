from harc_rag.routing.models import RoutingDecision


class AdaptiveRouter:

    def __init__(
        self,
        threshold: float = 0.65,
    ):
        self.threshold = threshold

    def route(
        self,
        confidence: float,
    ) -> RoutingDecision:

        if confidence < self.threshold:

            return RoutingDecision(
                should_verify=True,
                confidence=confidence,
                reason="Low confidence",
            )

        return RoutingDecision(
            should_verify=False,
            confidence=confidence,
            reason="High confidence",
        )