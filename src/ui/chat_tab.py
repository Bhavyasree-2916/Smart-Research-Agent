import streamlit as st

from src.rag.retriever import retriever
from src.services.chat_service import chat_service


def render_chat_tab():

    st.subheader("💬 Chat with Research")

    if not st.session_state.get("research_ready"):

        st.warning(
            "⚠ Please complete the Research step first."
        )

        return

    question = st.text_input(
        "Ask a question about your research"
    )

    if st.button(
        "Ask AI",
        use_container_width=True,
        type="primary"
    ):

        if question.strip() == "":

            st.error("Enter a question.")

            return

        context = retriever.retrieve(
            question,
            top_k=4
        )

        with st.spinner("🤖 Thinking..."):

            answer = chat_service.ask(
                question,
                context
            )

        st.success(answer)