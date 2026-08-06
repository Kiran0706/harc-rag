from harc_rag.pipeline.pipeline import HARCRAGPipeline


class PipelineService:

    def __init__(
        self,
        retriever,
    ):

        self.pipeline = HARCRAGPipeline(
            retriever
        )

    def ask(
        self,
        question: str,
    ) -> str:

        return self.pipeline.answer(
            question
        )