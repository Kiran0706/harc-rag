from dataclasses import dataclass


@dataclass
class RoutingDecision:

    should_verify: bool

    confidence: float

    reason: str