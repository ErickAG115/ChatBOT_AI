from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# data retreiver agent
# data retreival
def get_retriever():
    db = FAISS.load_local("vectorstore/faiss_index", HuggingFaceEmbeddings(), allow_dangerous_deserialization=True)
    return db.as_retriever()

# agent generation
def retriever_agent():
    llm = Ollama(model="mistral")
    retriever = get_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain