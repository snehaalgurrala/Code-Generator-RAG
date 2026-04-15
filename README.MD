# Code Generator RAG System

A modular Retrieval-Augmented Generation (RAG) system built with LangChain, FAISS, and Google Gemini.

## Features
- **Document Loading**: Supports `.pdf` and `.txt` files.
- **Vector Database**: Uses FAISS for local vector storage and fast retrieval.
- **LLM**: Powered by Google Gemini (`gemini-1.5-flash`).
- **Modular Code**: Separate files for loading, indexing, and querying logic.

## Project Structure
```
Code-Generator-RAG/
├── data/               # Drop your PDF/Text files here
├── vectorstore/        # FAISS index persistence (locally saved)
├── src/
│   ├── loader.py       # Loading & splitting documents
│   ├── vector_store.py # FAISS & Embeddings management
│   └── rag_chain.py    # LangChain RAG pipeline
├── main.py             # CLI Entry point
├── .env                # API Keys
└── requirements.txt    # Dependencies
```

## Setup & Usage

### 1. Installation
Ensure you have a virtual environment activated:
```bash
pip install -r requirements.txt
```

### 2. Configuration
Add your **Google API Key** to the `.env` file:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Add Data
Place any PDF or text files you want to query in the `data/` folder.

### 4. Run the Application
```bash
python main.py
```

## How it Works
1. **Load**: Documents are loaded from `data/`.
2. **Split**: Documents are chunked into smaller pieces.
3. **Embed**: Chunks are converted into vectors using Google Gemini Embeddings.
4. **Index**: Vectors are stored in a FAISS index.
5. **Query**: Users ask questions; the system retrieves relevant chunks and uses Gemini to generate an answer.
