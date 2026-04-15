import os
from dotenv import load_dotenv
from src.loader import load_documents, split_documents
from src.vector_store import get_vector_store, load_vector_store
from src.rag_chain import get_rag_chain

load_dotenv()

def main():
    data_path = "data"
    vectorstore_path = "vectorstore"
    
    # 1. Check for documents
    print("Checking for documents in 'data/' folder...")
    documents = load_documents(data_path)
    
    if not documents:
        print("No documents found in 'data/'. Please add some PDF or TXT files and try again.")
        # If vectorstore exists, we can still query, but let's assume we need to index first for this demo.
        if not os.path.exists(vectorstore_path):
            return
    
    # 2. Vector Store Setup
    if not os.path.exists(os.path.join(vectorstore_path, "index.faiss")):
        print("Creating new vector store index...")
        chunks = split_documents(documents)
        vector_store = get_vector_store(chunks, storage_path=vectorstore_path)
    else:
        print("Loading existing vector store index...")
        vector_store = load_vector_store(storage_path=vectorstore_path)
        
    if not vector_store:
        print("Error: Could not initialize vector store.")
        return

    # 3. Initialize RAG Chain
    print("Initializing RAG pipeline with Gemini...")
    rag_chain = get_rag_chain(vector_store)
    
    # 4. Interactive Loop
    print("\n--- Gemini RAG System Ready ---")
    print("Type 'exit' or 'quit' to stop.")
    
    while True:
        query = input("\nUser: ")
        if query.lower() in ["exit", "quit"]:
            break
        
        if not query.strip():
            continue
            
        print("Gemini is thinking...")
        try:
            result = rag_chain.invoke({"query": query})
            answer = result["result"]
            print(f"\nAssistant: {answer}")
            
            # Show sources if available
            sources = result.get("source_documents", [])
            if sources:
                print("\nSources:")
                for i, doc in enumerate(sources):
                    print(f"- {doc.metadata.get('source', 'Unknown')} (Chunk {i+1})")
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
