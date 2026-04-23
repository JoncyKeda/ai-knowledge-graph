import streamlit as st
from utils.extractor import extract_entities
from utils.graph_builder import build_graph

st.title("🧠 AI Knowledge Graph Builder")

text = st.text_area("Paste your document text:")

if st.button("Build Knowledge Graph"):
    entities = extract_entities(text)
    graph = build_graph(entities)

    st.subheader("🔗 Extracted Entities")
    st.write(entities)

    st.subheader("📊 Graph Connections")
    st.write(graph.edges())
