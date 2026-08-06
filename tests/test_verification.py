from harc_rag.verification.service import VerificationService


def test_verification():

    service = VerificationService()

    result = service.verify(

        question="What is TCP?",

        answer="TCP is a transport protocol.",

        context="TCP is a transport protocol.",

    )

    assert result.is_verified

    assert result.verified_answer == "TCP is a transport protocol."