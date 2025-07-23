import pickle
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# 1. 텍스트 파일 로드
loader = TextLoader("/Users/jangjuyeong/Downloads/장주영/무제 폴더/무제 폴더/장주영/medical_sample.txt")

# 2. 문서 불러오기
documents = loader.load()

# 3. 문서 분할: chunk_size=500, chunk_overlap=50
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# 4. docs.pkl로 저장
with open("docs.pkl", "wb") as f:
    pickle.dump(docs, f)

print("docs.pkl 파일 생성 완료!")

