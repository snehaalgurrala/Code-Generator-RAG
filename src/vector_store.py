import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_vector_store(chunks, storage_path="vectorstore"):
    """
    Create a vector store from document chunks using Google Gemini embeddings.
    Saves the index locally for persistence.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)
    
    # Create the vector store
    vector_store = FAISS.from_documents(chunks, embeddings)
    
    # Save the index locally
    vector_store.save_local(storage_path)
    return vector_store

def load_vector_store(storage_path="vectorstore"):
    """
    Load an existing FAISS index from the local storage.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    
    if os.path.exists(os.path.join(storage_path, "index.faiss")):
        return FAISS.load_local(storage_path, embeddings, allow_dangerous_deserialization=True)
    return None

def retrieve_relevant_docs(vector_store, query, k=3):
    """
    Search for and return the top 'k' most relevant documents for a query.
    """
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(query)
