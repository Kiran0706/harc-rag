from harc_rag.chunking.models import Chunk


class PromptBuilder:

    SYSTEM_PROMPT = """
You are an expert AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
reply with:

"I don't have enough information from the provided documents."

Do not make up facts.
"""

    def build(
        self,
        query: str,
        chunks: list[Chunk],
    ) -> str:

        context = "\n\n".join(
            chunk.text
            for chunk in chunks
        )

        return f"""
{self.SYSTEM_PROMPT}

Context
========
{context}

Question
========
{query}

Answer
========
"""