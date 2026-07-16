from src.research.search import search_topic
from src.research.scraper import extract_text

from src.rag.chunker import chunk_text
from src.rag.embeddings import embedding_model
from src.rag.vector_store import vector_store


class ResearchPipeline:

    def build_knowledge_base(self, topic, progress_callback=None):

        # ----------------------------
        # Step 1 : Search
        # ----------------------------
        if progress_callback:
            progress_callback("🔍 Searching the web...", 10)

        search_results = search_topic(topic)

        all_chunks = []

        sources = []
        if progress_callback:
            progress_callback("📄 Extracting article content...", 30)

        # ----------------------------
        # Step 2 : Scrape + Chunk
        # ----------------------------

        for index, result in enumerate(search_results, start=1):
            if progress_callback:
                progress_callback(
                    f"📄 Extracting article {index} of {len(search_results)}...",
                    20 + int((index / len(search_results)) * 30)
                )

            article = extract_text(result["link"])

            chunks = chunk_text(article)

            all_chunks.extend(chunks)

            sources.append(result)
        if progress_callback:
            progress_callback("✂️ Chunking completed. Creating embeddings...", 60)

        # ----------------------------
        # Step 3 : Embeddings
        # ----------------------------

        embeddings = embedding_model.create_embeddings(all_chunks)
        if progress_callback:
            progress_callback("🧠 Embeddings created. Building FAISS index...", 85)

        # ----------------------------
        # Step 4 : Vector Database
        # ----------------------------

        vector_store.create_index(
            embeddings,
            all_chunks
        )

        vector_store.save()
        if progress_callback:
            progress_callback("✅ Knowledge Base Ready!", 100)

        return {
            "success": True,
            "topic": topic,
            "status": "Knowledge Base Created Successfully",
            "sources": sources,
            "chunk_count": len(all_chunks),
            "embedding_count": len(embeddings)
            }


pipeline = ResearchPipeline()