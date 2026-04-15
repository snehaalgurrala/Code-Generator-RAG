import os
from dotenv import load_dotenv
from src.loader import load_documents, split_documents
from src.vector_store import get_vector_store, load_vector_store, retrieve_relevant_docs

# Load environment variables (for API key)
load_dotenv()

def run_test():
    data_path = "data"
    vectorstore_path = "vectorstore"
    
    # 1. Ensure the vector store exists and is up to date
    print("Step 1: Checking/Updating Vector Store...")
    docs = load_documents(data_path)
    if not docs:
        print("No documents found in 'data/'. Please ensure 'data/even_odd.py' exists.")
        return

    chunks = split_documents(docs)
    
    # Re-create/Update the index to include our new file
    print("Creating/Updating FAISS index...")
    vector_store = get_vector_store(chunks, storage_path=vectorstore_path)
    
    # 2. Perform the specific test retrieval
    query = 'even odd in python'
    print(f"\nStep 2: Querying the Retriever for: '{query}'")
    
    # Retrieve the top relevant chunk
    results = retrieve_relevant_docs(vector_store, query, k=1)
    
    if results:
        print("\n" + "="*30)
        print("✅ RELEVANT CODE FOUND")
        print("="*30)
        print(f"File Source: {results[0].metadata.get('source')}")
        print("\nContent:")
        print("-" * 20)
        print(results[0].page_content)
        print("-" * 20)
    else:
        print("\n❌ No relevant code found in the database.")

if __name__ == "__main__":
    # Ensure you have your GOOGLE_API_KEY in .env before running
    run_test()
