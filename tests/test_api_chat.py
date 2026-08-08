from fastapi.testclient import TestClient

from harc_rag.api.main import app
from harc_rag.api.routes import set_pipeline


class FakePipeline:

    def answer(self, question: str) -> str:

        return f"Answer for: {question}"


def test_chat():

    set_pipeline(FakePipeline())

    client = TestClient(app)

    response = client.post(
        "/chat",
        json={
            "question": "What is TCP?"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data

    assert data["answer"] == "Answer for: What is TCP?"