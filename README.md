# 🧠 의료 논문 기반 RAG 실습

이 저장소는 RAG(Retrieval-Augmented Generation) 구조를 간단히 구현해보기 위한 실습 프로젝트입니다.  
의료 관련 텍스트 데이터를 기반으로 FAISS 벡터 검색과 언어 모델을 결합하여 질문 응답(QA) 기능을 테스트해보았습니다.

---

## 📌 실습 내용

- 논문 텍스트 데이터를 전처리하여 문장 단위로 나눔
- `sentence-transformers`를 이용해 임베딩 생성
- FAISS를 사용해 벡터 인덱스 구축
- 검색 결과를 바탕으로 LLM에 질문 응답 요청
- Streamlit을 활용한 간단한 QA 데모 구현

---

## 🛠 사용한 기술

- Python
- FAISS
- sentence-transformers
- Hugging Face Transformers
- Streamlit
- Jupyter Notebook

---

## 🗂 파일 구성

├── 논문요약.ipynb # 논문 데이터 전처리 실습
├── build_vector_index.ipynb # 임베딩 및 인덱스 생성
├── rag_pipeline.py # 검색 + 생성 파이프라인
├── app.py # Streamlit 데모
├── medical_sample.txt # 샘플 논문 텍스트
└── requirements.txt # 의존성 목록

---

## 📑 후기
처음으로 RAG 구조를 직접 구현해보며 검색 기반 QA의 흐름을 이해할 수 있었던 실습이었습니다.
데이터 전처리, 임베딩, 벡터 검색, 언어 모델 연결까지의 과정을 단계별로 체험해본 것이 인상 깊었습니다.
