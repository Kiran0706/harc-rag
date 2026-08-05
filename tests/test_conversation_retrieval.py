from harc_rag.memory.models import (
    Conversation,
    Message,
)

from harc_rag.retrieval.conversation_retriever import (
    ConversationRetriever,
)


class DummyRetriever:

    def retrieve(self, query, k=5):
        return query


def test_conversation_retrieval():

    conversation = Conversation(
        conversation_id="chat1"
    )

    conversation.messages.append(
        Message(
            role="user",
            content="Explain TCP"
        )
    )

    retriever = ConversationRetriever(
        DummyRetriever()
    )

    query = retriever.retrieve(
        conversation,
        "How many packets are exchanged?"
    )

    assert "Explain TCP" in query

    assert "How many packets" in query