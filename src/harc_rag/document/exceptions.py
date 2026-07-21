class DocumentLoaderError(Exception):
    """Base exception for document loading."""


class UnsupportedFileTypeError(DocumentLoaderError):
    """Raised when an unsupported file type is provided."""


class EmptyDocumentError(DocumentLoaderError):
    """Raised when a document contains no extractable text."""