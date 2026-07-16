import streamlit as st

from src.services.citation_service import citation_service


def render_citation_tab():

    st.subheader("📚 Citations")

    if not st.session_state.get("research_ready"):

        st.info("Complete Research first.")

        return

    style = st.selectbox(

        "Citation Style",

        [

            "APA",

            "MLA",

            "IEEE"

        ]

    )

    if st.button("Generate Citations"):

        if style == "APA":

            citations = citation_service.generate_apa(

                st.session_state["sources"]

            )

        elif style == "MLA":

            citations = citation_service.generate_mla(

                st.session_state["sources"]

            )

        else:

            citations = citation_service.generate_ieee(

                st.session_state["sources"]

            )

        st.subheader(style + " Citations")

        for citation in citations:

            st.code(citation)
            
        st.session_state["citations"] = citations