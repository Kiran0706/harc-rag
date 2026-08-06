from dataclasses import dataclass


@dataclass
class ConfidenceScore:

    retrieval: float

    generation: float

    evidence: float


@dataclass
class JointUncertainty:

    confidence: ConfidenceScore

    score: float

    should_verify: bool