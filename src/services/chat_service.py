from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


class ChatService:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def ask(self, question, context):

        prompt = f"""
You are an AI Research Assistant.

Answer ONLY using the provided context.

If the answer is not available in the context,
say:

"I couldn't find that information in the research."

-----------------------

Context:

{context}

-----------------------

Question:

{question}

Give a clear, professional answer.
"""

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3

        )

        return response.choices[0].message.content


chat_service = ChatService()