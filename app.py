import streamlit as st

from rag_pipeline import generate_answer


st.set_page_config(
    page_title="RefraScan RAG Assistant",
    page_icon="👁️",
    layout="centered"
)

st.title("👁️ RefraScan RAG Assistant")
st.write(
    "Ask questions about the RefraScan thesis using a local "
    "TF-IDF retrieval system and Ollama."
)

st.info(
    "This application uses the RefraScan knowledge base for retrieval "
    "and a locally running Llama 3.2 model for answer generation."
)

query = st.text_input(
    "Ask a question about RefraScan:",
    placeholder="Example: What are the three refractive status classes?"
)

if st.button("Ask"):
    if query.strip():
        with st.spinner("Retrieving information and generating answer..."):
            answer, results = generate_answer(query)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Retrieved Sources")

        for i, result in enumerate(results, start=1):
            with st.expander(
                f"Source {i} — Similarity: {result['score']:.4f}"
            ):
                st.write(result["text"])
    else:
        st.warning("Please enter a question first.")