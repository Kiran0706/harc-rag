from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class SemanticSimilarity:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ):
        self.model = SentenceTransformer(model_name)

    def similarity(
        self,
        text1: str,
        text2: str,
    ) -> float:

        embedding1 = self.model.encode(
            text1,
            convert_to_tensor=True,
        )

        embedding2 = self.model.encode(
            text2,
            convert_to_tensor=True,
        )

        score = cos_sim(
            embedding1,
            embedding2,
        )

        return float(score)