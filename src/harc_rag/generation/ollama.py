from ollama import Client

from harc_rag.generation.interfaces import LLM
from harc_rag.generation.exceptions import GenerationError


class OllamaLLM(LLM):

    def __init__(
        self,
        model: str = "qwen2.5:3b",
        host: str = "http://localhost:11434",
    ):
        self.model = model
        self.client = Client(host=host)

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.generate(
                model=self.model,
                prompt=prompt,
            )

            return response["response"]

        except Exception as exc:
            raise GenerationError(str(exc)) from exc