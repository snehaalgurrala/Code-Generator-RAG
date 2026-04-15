import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents(data_path: str):
    """
    Load documents from the specified directory.
    Supports .pdf, .txt, and code files (.py, .js, etc.)
    """
    if not os.path.exists(data_path):
        print(f"Directory {data_path} does not exist.")
        return []

    documents = []
    
    # Text and Code files
    extensions = ["*.txt", "*.py", "*.js", "*.html", "*.css", "*.md"]
    for ext in extensions:
        loader = DirectoryLoader(data_path, glob=f"./{ext}", loader_cls=TextLoader)
        documents.extend(loader.load())
    
    # PDF files
    pdf_loader = DirectoryLoader(data_path, glob="./*.pdf", loader_cls=PyPDFLoader)
    documents.extend(pdf_loader.load())
    
    print(f"Loaded {len(documents)} total documents.")
    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=150):
    """
    Split documents into smaller chunks for embedding.
    Uses RecursiveCharacterTextSplitter for optimal context preservation.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""] # Priority splitting order
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(chunks)} chunks.")
    return chunks
