class ChunkingError(Exception):
    """Base exception for all chunking-related errors."""
    pass


class InvalidChunkConfigurationError(ChunkingError):
    """Raised when chunk_size or chunk_overlap is invalid."""
    pass