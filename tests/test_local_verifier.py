from harc_rag.verification.verifier import LocalVerifier


class FakeLLM:

    def generate(self, prompt):

        return "TCP uses a three-way handshake."


def test_local_verifier():

    verifier = LocalVerifier()

    verifier.llm = FakeLLM()

    result = verifier.verify(

        question="How does TCP connect?",

        answer="TCP uses a four-way handshake.",

        context="TCP uses a three-way handshake.",

    )

    assert result.verified_answer == "TCP uses a three-way handshake."