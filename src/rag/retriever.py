from src.rag.embeddings import embedding_model
from src.rag.vector_store import vector_store


class Retriever:

    def retrieve(self, query, top_k=5):

        # Load FAISS if not already loaded
        if vector_store.index is None:
            vector_store.load()

        query_embedding = embedding_model.create_embeddings(
            [query]
        )

        results = vector_store.search(
            query_embedding,
            top_k
        )

        return "\n\n".join(results)


retriever = Retriever()