from harc_rag.verification.models import VerificationResult


class LocalVerifier:

    def verify(
        self,
        question: str,
        answer: str,
        context: str,
    ) -> VerificationResult:

        return VerificationResult(
            original_answer=answer,
            verified_answer=answer,
            is_verified=True,
            confidence=1.0,
        )