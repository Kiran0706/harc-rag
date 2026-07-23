class VectorStoreError(Exception):
    """Base exception for vector store."""


class EmptyIndexError(VectorStoreError):
    """Raised when searching an empty index."""