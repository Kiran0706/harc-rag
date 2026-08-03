from harc_rag.memory.context_builder import ContextBuilder
from harc_rag.memory.models import Conversation, Message


def test_context_builder():

    conversation = Conversation(
        conversation_id="chat1"
    )

    conversation.messages.append(
        Message(
            role="user",
            content="What is TCP?"
        )
    )

    conversation.messages.append(
        Message(
            role="assistant",
            content="TCP is a transport protocol."
        )
    )

    builder = ContextBuilder()

    context = builder.build(conversation)

    assert "What is TCP?" in context
    assert "TCP is a transport protocol." in context