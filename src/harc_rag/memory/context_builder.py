from harc_rag.memory.models import Conversation


class ContextBuilder:

    def build(
        self,
        conversation: Conversation,
    ) -> str:

        if not conversation.messages:
            return ""

        history = []

        for message in conversation.messages:

            history.append(
                f"{message.role.title()}: {message.content}"
            )

        return "\n".join(history)