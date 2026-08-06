from harc_rag.generation.generator import RAGGenerator
from harc_rag.generation.service import GenerationService
from harc_rag.generation.prompt_builder import PromptBuilder

from harc_rag.routing.router import AdaptiveRouter
from harc_rag.uncertainty.estimator import JointEstimator
from harc_rag.verification.verifier import LocalVerifier


class HARCRAGPipeline:

    def __init__(
        self,
        retriever,
    ):

        self.retriever = retriever

        self.prompt_builder = PromptBuilder()

        self.generator = RAGGenerator(
            GenerationService()
        )

        self.estimator = JointEstimator()

        self.router = AdaptiveRouter()

        self.verifier = LocalVerifier()

    def answer(
        self,
        question: str,
    ) -> str:

        # Retrieve relevant chunks
        retrieval_results = self.retriever.retrieve(question)

        chunks = [
            result.chunk
            for result in retrieval_results
        ]

        context = "\n".join(
            chunk.text
            for chunk in chunks
        )

        # Build prompt
        prompt = self.prompt_builder.build(
            query=question,
            chunks=chunks,
        )

        # Generate answer
        answer = self.generator.generate(prompt)

        # Estimate uncertainty
        uncertainty = self.estimator.estimate(
            retrieval_results,
            answer,
            context,
        )

        # Decide whether verification is required
        decision = self.router.route(
            uncertainty.score
        )

        if decision.should_verify:

            verification = self.verifier.verify(
                question,
                answer,
                context,
            )

            return verification.verified_answer

        return answer