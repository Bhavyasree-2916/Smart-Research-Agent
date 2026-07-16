import os
import pickle
import faiss
import numpy as np

from src.utils.config import VECTOR_DB_DIR


class VectorStore:

    def __init__(self):
        self.index = None
        self.chunks = []

    def create_index(self, embeddings, chunks):
        """
        Create a FAISS index from embeddings.
        """

        if len(embeddings) == 0:
            return

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            np.array(embeddings).astype("float32")
        )

        self.chunks = chunks

    def save(self):

        os.makedirs(VECTOR_DB_DIR, exist_ok=True)

        faiss.write_index(
            self.index,
            str(VECTOR_DB_DIR / "research.index")
        )

        with open(
            VECTOR_DB_DIR / "chunks.pkl",
            "wb"
        ) as file:

            pickle.dump(self.chunks, file)

    def load(self):

        self.index = faiss.read_index(
            str(VECTOR_DB_DIR / "research.index")
        )

        with open(
            VECTOR_DB_DIR / "chunks.pkl",
            "rb"
        ) as file:

            self.chunks = pickle.load(file)

    def search(self, query_embedding, top_k=5):

        distances, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )

        results = []

        for index in indices[0]:

            if index < len(self.chunks):

                results.append(self.chunks[index])

        return results


# Singleton Instance
vector_store = VectorStore()