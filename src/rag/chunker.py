from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.utils.config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_text(text: str):
    """
    Split extracted article text into overlapping chunks for RAG.
    """

    if not text:
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        is_separator_regex=False
    )

    chunks = splitter.split_text(text)

    return chunks