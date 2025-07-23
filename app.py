import streamlit as st
from transformers import pipeline
import faiss
import numpy as np
import pickle

# 로드된 인덱스와 문서 불러오기
with open("docs.pkl", "rb") as f:
    documents = pickle.load(f)

index = faiss.read_index("vector.index")
embed = pipeline("feature-extraction", model="sentence-transformers/all-MiniLM-L6-v2")
qa = pipeline("text2text-generation", model="t5-small")

def search(query, top_k=3):
    q_vec = np.array(embed(query))[0].mean(0).reshape(1, -1).astype('float32')
    scores, indices = index.search(q_vec, top_k)
    return [documents[i] for i in indices[0]]

st.title("의료 문서 기반 QA 시스템")
query = st.text_input("질문을 입력하세요")

if query:
    context = "\n".join(search(query))
    prompt = f"context: {context} question: {query}"
    answer = qa(prompt, max_length=128, do_sample=False)[0]['generated_text']
    st.subheader("답변")
    st.write(answer)