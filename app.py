import streamlit as st
from src.ui.citation_tab import render_citation_tab
from src.ui.research_tab import render_research_tab
from src.ui.brief_tab import render_brief_tab
from src.ui.quiz_tab import render_quiz_tab
from src.ui.export_tab import render_export_tab
from src.ui.chat_tab import render_chat_tab

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
        
st.set_page_config(
    page_title="Smart Research Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

st.markdown("""
<div style="text-align:center;padding:25px 0px;">

<h1 style="font-size:48px;margin-bottom:0px;">
🔬 ResearchIQ
</h1>

<h3 style="color:gray;margin-top:5px;">
AI Powered Smart Research Platform
</h3>

<p style="font-size:18px;color:#666;">
Search • Summarize • Cite • Learn
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex;
justify-content:space-around;
margin-top:25px;
margin-bottom:25px;">

<div style="
background:white;
padding:18px;
border-radius:12px;
width:22%;
box-shadow:0 4px 10px rgba(0,0,0,.08);
text-align:center;">

🌐
<h4>Research</h4>
<p>Search real web content</p>

</div>

<div style="
background:white;
padding:18px;
border-radius:12px;
width:22%;
box-shadow:0 4px 10px rgba(0,0,0,.08);
text-align:center;">

📄
<h4>Brief</h4>
<p>LLM generated summary</p>

</div>

<div style="
background:white;
padding:18px;
border-radius:12px;
width:22%;
box-shadow:0 4px 10px rgba(0,0,0,.08);
text-align:center;">

📚
<h4>Citations</h4>
<p>APA • MLA • IEEE</p>

</div>

<div style="
background:white;
padding:18px;
border-radius:12px;
width:22%;
box-shadow:0 4px 10px rgba(0,0,0,.08);
text-align:center;">

📝
<h4>Quiz</h4>
<p>AI Generated MCQs</p>

</div>

</div>
""", unsafe_allow_html=True)

with st.expander("ℹ️ About this Project"):

    st.markdown("""
### Smart Research Agent

This application demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline.

### Workflow

1. 🌐 Search the web for relevant information.
2. 📄 Extract content from trusted websites.
3. ✂️ Split content into chunks.
4. 🧠 Generate embeddings using Sentence Transformers.
5. 💾 Store embeddings in a FAISS vector database.
6. 🔍 Retrieve relevant context.
7. 🤖 Generate research briefs using Groq LLM.
8. 📚 Generate citations.
9. 📝 Generate quizzes.

### Tech Stack

- Python
- Streamlit
- Groq LLM
- FAISS
- Sentence Transformers
- DDGS Search
- Trafilatura
""")

st.caption("AI Powered Research Assistant using LLMs + RAG")
with st.sidebar:

    st.title("🔬 Smart Research Agent")

    st.success("🟢 System Online")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.write("🐍 Python")
    st.write("🤖 Groq")
    st.write("🧠 BGE Embeddings")
    st.write("📚 FAISS")
    st.write("🌐 DDGS")
    st.write("⚡ Streamlit")

    st.markdown("---")

    st.subheader("📊 Features")

    st.write("✅ Research")
    st.write("✅ Brief")
    st.write("✅ Citations")
    st.write("✅ Quiz")
    st.write("✅ Export")

    st.markdown("---")

    st.caption("Version 1.0")
    
    st.success("🎉 Research completed successfully. The knowledge base is ready for AI analysis.")
    
    st.markdown("---")

st.subheader("📊 Session")

if "research_ready" in st.session_state:

    st.success("Knowledge Base Ready")

else:

    st.warning("No Research Yet")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔍 Research",
    "📄 Brief",
    "📚 Citations",
    "📝 Quiz",
    "💬 Chat",
    "📥 Export"
])


with tab1:

    render_research_tab()

with tab2:

    render_brief_tab()

with tab3:
    render_citation_tab()

with tab4:
    render_quiz_tab()
    
with tab5:
    render_chat_tab()

with tab6:
    render_export_tab()
    
st.markdown("---")

st.markdown("""
<div style="text-align:center;color:gray;">

Built with ❤️ using

Python • Streamlit • Groq • FAISS • Sentence Transformers

</div>
""", unsafe_allow_html=True)