from src.ai.groq_client import groq_client
from src.rag.retriever import retriever


class QuizService:

    def generate_quiz(self, topic, difficulty, num_questions):

        chunks = retriever.retrieve(
            topic,
            top_k=5
        )

        context = "\n\n".join(chunks)

        prompt = f"""
You are an expert educator.

Generate {num_questions} multiple-choice questions.

Topic:
{topic}

Difficulty:
{difficulty}

Context:
{context}

Instructions:

1. Each question must have exactly four options.
2. Mark the correct answer clearly.
3. Give a one-line explanation after every answer.
4. Format using Markdown.

Example:

## Question 1

What is AI?

A.

B.

C.

D.

**Correct Answer:** B

**Explanation:** ...
"""

        return groq_client.generate(prompt)


quiz_service = QuizService()