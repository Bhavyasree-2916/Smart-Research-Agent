from src.ai.groq_client import groq_client
from src.rag.retriever import retriever


class BriefService:

    def generate_brief(self, topic):

        relevant_chunks = retriever.retrieve(
            topic,
            top_k=5
        )

        context = "\n\n".join(relevant_chunks)

        prompt = f"""
You are a senior research analyst.

Generate a professional research report.

Topic:
{topic}

Context:
{context}

The report must contain the following sections.

# Overview

# Key Concepts

# Important Findings

# Real World Applications

# Advantages

# Challenges

# Future Scope

# Conclusion

Write in clear professional English.

Use bullet points wherever appropriate.

Do not invent information outside the provided context.
"""

        return groq_client.generate(prompt)


brief_service = BriefService()