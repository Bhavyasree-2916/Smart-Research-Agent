import streamlit as st

from src.services.export_service import export_service


def render_export_tab():

    st.subheader("📥 Export Report")

    if "brief" not in st.session_state:

        st.info("Generate a Research Brief first.")

        return

    report = export_service.generate_markdown(

        topic=st.session_state["research_topic"],

        brief=st.session_state["brief"],

        citations=st.session_state.get("citations"),

        quiz=st.session_state.get("quiz")

    )

    st.download_button(

        "📄 Download Research Report",

        report,

        file_name="research_report.md",

        mime="text/markdown",

        use_container_width=True

    )