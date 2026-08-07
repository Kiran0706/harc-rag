from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import string


class SemanticSimilarity:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ):
        self.model_name = model_name
        self.model = None

    def similarity(
        self,
        text1: str,
        text2: str,
    ) -> float:
        try:
            return self._semantic_similarity(
                text1,
                text2,
            )
        except Exception:
            return self._lexical_similarity(
                text1,
                text2,
            )

    def _semantic_similarity(
        self,
        text1: str,
        text2: str,
    ) -> float:
        if self.model is None:
            self.model = SentenceTransformer(self.model_name)

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

    def _lexical_similarity(
        self,
        text1: str,
        text2: str,
    ) -> float:
        words1 = self._normalized_words(text1)
        words2 = self._normalized_words(text2)

        if not words1 or not words2:
            return 0.0

        return len(words1 & words2) / min(len(words1), len(words2))

    def _normalized_words(
        self,
        text: str,
    ) -> set[str]:
        translator = str.maketrans("", "", string.punctuation)
        words = text.lower().translate(translator).split()

        return {
            self._stem(word)
            for word in words
        }

    def _stem(
        self,
        word: str,
    ) -> str:
        if word == "using":
            return "use"

        for suffix in ("ing", "es", "s"):
            if len(word) > len(suffix) + 2 and word.endswith(suffix):
                return word[: -len(suffix)]

        return word
