import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def test_embeddings():
    try:
        print("Testing with gemini-embedding-001:")
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        texts = ["Hello world", "This is a test", "Another document"]
        result = embeddings.embed_documents(texts)
        print(f"Number of texts: {len(texts)}")
        print(f"Number of embeddings returned: {len(result)}")
        
        print("\nTesting with gemini-embedding-2-preview:")
        embeddings2 = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
        result2 = embeddings2.embed_documents(texts)
        print(f"Number of texts: {len(texts)}")
        print(f"Number of embeddings returned: {len(result2)}")
    except Exception as e:
        print(f"Error during embedding: {e}")

if __name__ == "__main__":
    test_embeddings()
