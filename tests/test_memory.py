from harc_rag.memory.manager import MemoryManager


def test_memory():

    manager = MemoryManager()

    manager.create("chat1")

    manager.add_message(
        "chat1",
        "user",
        "What is TCP?",
    )

    conversation = manager.get("chat1")

    assert len(conversation.messages) == 1

    assert conversation.messages[0].content == "What is TCP?"