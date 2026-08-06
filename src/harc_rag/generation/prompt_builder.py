from harc_rag.chunking.models import Chunk


class PromptBuilder:

    SYSTEM_PROMPT = """
You are an expert AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
reply:

"I don't have enough information from the provided documents."

Do not hallucinate.
"""

    def build(
        self,
        query: str,
        chunks: list[Chunk],
        conversation_context: str = "",
    ) -> str:

        context = "\n\n".join(
            chunk.text
            for chunk in chunks
        )

        return f"""
{self.SYSTEM_PROMPT}

Conversation History
====================

{conversation_context}

Retrieved Context
=================

{context}

Current Question
================

{query}

Answer
=======
"""