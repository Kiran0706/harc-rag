from pathlib import Path

from pypdf import PdfReader

from .exceptions import (
    EmptyDocumentError,
    UnsupportedFileTypeError,
)
from .models import Document


class DocumentLoader:
    """
    Loads supported document types.
    """

    SUPPORTED_EXTENSIONS = {".pdf"}

    def load(self, file_path: str) -> Document:

        path = Path(file_path)

        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise UnsupportedFileTypeError(path.suffix)

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        if not text.strip():
            raise EmptyDocumentError(path.name)

        return Document(
            file_name=path.name,
            file_path=path,
            text=text,
            page_count=len(reader.pages),
            metadata={
                "source": path.name,
                "loader": "pypdf",
                "language": "unknown",
            },
        )