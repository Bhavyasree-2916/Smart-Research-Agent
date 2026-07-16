from sentence_transformers import SentenceTransformer
from src.utils.config import EMBEDDING_MODEL


class EmbeddingModel:

    def __init__(self):
        """
        Load the embedding model only once.
        """
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def create_embeddings(self, chunks):
        """
        Convert text chunks into embeddings.
        """

        if not chunks:
            return []

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings


# Singleton Instance
embedding_model = EmbeddingModel()