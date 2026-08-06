from abc import ABC, abstractmethod

from harc_rag.verification.models import VerificationResult


class Verifier(ABC):

    @abstractmethod
    def verify(
        self,
        question: str,
        answer: str,
        context: str,
    ) -> VerificationResult:
        pass