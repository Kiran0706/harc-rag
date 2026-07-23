import faiss
import numpy as np

from harc_rag.embedding.models import Embedding
from harc_rag.vectorstore.exceptions import EmptyIndexError
from harc_rag.vectorstore.interfaces import VectorStore
from harc_rag.vectorstore.models import SearchResult


class FAISSVectorStore(VectorStore):

    def __init__(self):
        self.index = None
        self.embeddings: list[Embedding] = []

    def add(self, embeddings: list[Embedding]) -> None:

        if not embeddings:
            return

        dimension = len(embeddings[0].vector)

        if self.index is None:
            self.index = faiss.IndexFlatL2(dimension)

        vectors = np.array(
            [embedding.vector for embedding in embeddings],
            dtype="float32",
        )

        self.index.add(vectors)

        self.embeddings.extend(embeddings)

    def search(
        self,
        query_vector: list[float],
        k: int = 5,
    ) -> list[SearchResult]:

        if self.index is None:
            raise EmptyIndexError("The vector store is empty.")

        query = np.array([query_vector], dtype="float32")

        distances, indices = self.index.search(query, k)

        results = []

        for distance, index in zip(distances[0], indices[0]):

            if index == -1:
                continue

            results.append(
                SearchResult(
                    embedding=self.embeddings[index],
                    score=float(distance),
                )
            )

        return results

    def save(self, path: str):
        faiss.write_index(self.index, path)

    def load(self, path: str):
        self.index = faiss.read_index(path)