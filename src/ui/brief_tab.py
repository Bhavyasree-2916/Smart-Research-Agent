import streamlit as st

from src.services.brief_service import brief_service


def render_brief_tab():

    st.subheader("📄 Research Brief")

    if not st.session_state.get("research_ready"):

        st.info(
            "Please complete Research first."
        )

        return

    if st.button(
        "Generate Brief",
        use_container_width=True
    ):

        with st.spinner("🤖 Groq is generating your research brief..."):

            brief = brief_service.generate_brief(

                st.session_state["research_topic"]

            )
            
        st.session_state["brief"] = brief

        st.success("✅ Research Brief Generated Successfully")
        st.divider()
        st.markdown(brief)
        
        st.download_button(
            label="📥 Download Research Brief",
            data=brief,
            file_name="research_brief.md",
            mime="text/markdown",
            use_container_width=True
            )