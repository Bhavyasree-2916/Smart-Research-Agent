import streamlit as st

from src.services.quiz_service import quiz_service


def render_quiz_tab():

    st.subheader("📝 Quiz Generator")

    if not st.session_state.get("research_ready"):

        st.info("Please complete Research first.")

        return

    difficulty = st.selectbox(

        "Difficulty",

        [

            "Easy",

            "Medium",

            "Hard"

        ]

    )

    questions = st.slider(

        "Number of Questions",

        5,

        20,

        10,

        step=5

    )

    if st.button(

        "Generate Quiz",

        use_container_width=True

    ):

        with st.spinner("Generating Quiz..."):

            quiz = quiz_service.generate_quiz(

                st.session_state["research_topic"],

                difficulty,

                questions

            )
            
        st.session_state["quiz"] = quiz

        st.success("✅ Quiz Generated Successfully")
        
        st.divider()

        st.markdown(quiz)

        st.download_button(
            label="📥 Download Quiz",
            data=quiz,
            file_name="quiz.md",
            mime="text/markdown",
            use_container_width=True
            )