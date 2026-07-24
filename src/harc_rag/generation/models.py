from dataclasses import dataclass


@dataclass
class GenerationRequest:
    prompt: str


@dataclass
class GenerationResponse:
    text: str