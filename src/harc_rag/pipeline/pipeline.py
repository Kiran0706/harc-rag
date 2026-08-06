from harc_rag.generation.generator import Generator
from harc_rag.routing.router import AdaptiveRouter
from harc_rag.uncertainty.estimator import JointEstimator
from harc_rag.verification.verifier import LocalVerifier


class HARCRAGPipeline:

    def __init__(
        self,
        retriever,
    ):

        self.retriever = retriever

        self.generator = Generator()

        self.estimator = JointEstimator()

        self.router = AdaptiveRouter()

        self.verifier = LocalVerifier()
        def answer(
        self,
        question: str,
    ) -> str:

        retrieval_results = self.retriever.retrieve(question)

        context = "\n".join(

            result.chunk.text

            for result in retrieval_results

        )

        answer = self.generator.generate(

            question,

            context,

        )

        uncertainty = self.estimator.estimate(

            retrieval_results,

            answer,

            context,

        )

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