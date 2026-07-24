from harc_rag.generation.service import GenerationService


class RAGGenerator:

    def __init__(self, generation_service: GenerationService):
        self.generation_service = generation_service

    def generate(self, prompt: str) -> str:
        return self.generation_service.generate(prompt)