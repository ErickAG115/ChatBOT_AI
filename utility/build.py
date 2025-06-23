from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import os

# pathfinder for the local data folder
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
texts = []
# file reading
for filename in os.listdir(data_path):
    if filename.endswith(".txt"):
        filepath = os.path.join(data_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            texts.append(f.read())
# document conversion
docs = [Document(page_content=text) for text in texts]
# text division into chunks
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = splitter.split_documents(docs)
print(f"Número de chunks creados: {len(splits)}")
# embedding creation
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# vectorsotre generation
vectorstore = FAISS.from_documents(splits, embeddings)
# local save
vectorstore.save_local("vectorstore/faiss_index")
print("Vectorstore creado y guardado correctamente.")