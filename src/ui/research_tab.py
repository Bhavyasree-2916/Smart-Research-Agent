import streamlit as st

from src.core.pipeline import pipeline


def render_research_tab():

    st.markdown("## 🔍 Research Module")

    st.info(
        """
        This module searches the web, extracts relevant information,
        creates a RAG knowledge base, and prepares the data for AI-powered analysis.
        """
    )

    with st.container(border=True):

        st.subheader("🔍 Research Topic")

        topic = st.text_input(
            "Enter your topic",
            key="topic"
        )

        if topic:
            st.success(f"📌 Current Topic: {topic}")

    st.divider()

    if st.button(
        "🚀 Start Research",
        use_container_width=True,
        type="primary"
    ):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
            return

        progress = st.progress(0)
        status = st.empty()

        def update_progress(message, value):
            status.info(message)
            progress.progress(value)

        result = pipeline.build_knowledge_base(
            topic,
            progress_callback=update_progress
        )

        status.success("✅ Knowledge Base Created Successfully!")

        st.session_state["research_ready"] = True
        st.session_state["research_topic"] = topic
        st.session_state["sources"] = result["sources"]

        st.success("🎉 Research completed successfully!")

        st.markdown("## 📊 Research Dashboard")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "🌐 Sources",
                len(result["sources"])
            )

        with col2:
            st.metric(
                "📄 Chunks",
                result["chunk_count"]
            )

        with col3:
            st.metric(
                "🧠 Embeddings",
                result["embedding_count"]
            )

        with col4:
            st.metric(
                "⚡ Status",
                "Ready"
            )

        st.divider()

        st.subheader("🌍 Research Sources")

        for i, source in enumerate(result["sources"], start=1):

            with st.container(border=True):

                st.markdown(f"### 📄 Source {i}")

                st.write(source["title"])

                st.link_button(
                    "Open Website",
                    source["link"],
                    use_container_width=True
                )

                st.divider()