
import streamlit as st
import faiss
from pathlib import Path
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import os

st.set_page_config(page_title="🔍 RAG Assistant", layout="centered")
st.title("🔍 Retrieval-Augmented Assistant")

# Load model + retriever once
@st.cache_resource
def load_resources():
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    model = pipeline("text-generation", model="./checkpoints/my_model")
    return embedder, model

embedder, model = load_resources()

# Load and chunk corpus
@st.cache_resource
def load_chunks(folder="data/corpus"):
    folder_path = Path(folder)
    files = list(folder_path.glob("*.md"))
    chunks = []
    sources = []
    for file in files:
        text = file.read_text()
        for para in text.split("\n\n"):
            if len(para.split()) > 20:
                chunks.append(para.strip())
                sources.append(file.name)
    embeddings = embedder.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return chunks, sources, index

chunks, sources, index = load_chunks()

# RAG query function
def rag_query(query, k=3):
    q_embed = embedder.encode([query])
    _, indices = index.search(q_embed, k)
    top_chunks = [chunks[i] for i in indices[0]]
    top_sources = [sources[i] for i in indices[0]]
    return top_chunks, top_sources

# Prompt formatting
def format_prompt(chunks, query):
    context = "\n\n".join(chunks)
    return f"Answer the following based only on the provided context.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

# Interface
query = st.text_area("Ask a question grounded in your docs:")

if st.button("Generate Answer") and query.strip():
    with st.spinner("Retrieving and generating..."):
        chunks_used, sources_used = rag_query(query)
        prompt = format_prompt(chunks_used, query)
        result = model(prompt, max_new_tokens=150)[0]["generated_text"]

    st.markdown("### ✍️ Answer")
    st.write(result)

    st.markdown("### 📚 Sources")
    st.markdown(", ".join(set(sources_used)))
