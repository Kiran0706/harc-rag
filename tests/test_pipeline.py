from harc_rag.pipeline.pipeline import HARCRAGPipeline
from harc_rag.chunking.models import Chunk
from harc_rag.retrieval.models import RetrievalResult


class FakeRetriever:

    def retrieve(
        self,
        query,
        k=5,
    ):

        return [

            RetrievalResult(

                chunk=Chunk(
                    chunk_id=1,
                    text="TCP uses a three-way handshake.",
                    start_index=0,
                    end_index=30,
                    metadata={},
                ),

                score=0.9,
            )

        ]


def test_pipeline_creation():

    pipeline = HARCRAGPipeline(
        FakeRetriever()
    )

    assert pipeline is not None