from harc_rag.generation.interfaces import LLM


class GenerationService:

    def __init__(self, llm: LLM):
        self.llm = llm

    def generate(self, prompt: str) -> str:
        return self.llm.generate(prompt)