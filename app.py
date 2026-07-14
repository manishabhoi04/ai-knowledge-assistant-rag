import streamlit as st

from rag_engine import ask_rag_with_sources

st.title("📚 RAG Chatbot")

question = st.text_input("Ask a Question")

if question:

    with st.spinner("Searching documents..."):

        answer, sources = ask_rag_with_sources(question)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")

    for source in sources:
        st.write(source)