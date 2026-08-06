from harc_rag.verification.verifier import LocalVerifier


class VerificationService:

    def __init__(self):

        self.verifier = LocalVerifier()

    def verify(
        self,
        question: str,
        answer: str,
        context: str,
    ):

        return self.verifier.verify(
            question,
            answer,
            context,
        )