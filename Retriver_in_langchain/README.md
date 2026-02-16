# Retriever in LangChain

This project demonstrates the implementation of a retrieval system using LangChain. It covers the complete workflow from document loading to information retrieval using vector databases.

## Features

- Document loading from Wikipedia and PDF files.
- Text splitting using Recursive Character Text Splitter.
- Embedding generation using Hugging Face Sentence Transformers.
- Vector storage with ChromaDB.
- Query retrieval based on semantic similarity.

## Prerequisites

- Python 3.x
- Groq API Key
- Hugging Face Token

## Installation

```bash
pip install langchain langchain-community pypdf chromadb langchain-text-splitters transformers langchain-groq wikipedia
```

## Workflow

1. **Load Documents**: Use `WikipediaLoader` or `PyPDFLoader` to ingest data from external sources.
2. **Split Text**: Break down large documents into smaller, manageable chunks (e.g., 1000 characters with 100-character overlap).
3. **Generate Embeddings**: Convert text chunks into numerical vectors using the `sentence-transformers/all-MiniLM-L6-v2` model.
4. **Vector Storage**: Store the embeddings in a ChromaDB collection for efficient searching.
5. **Retrieval**: Use the vector store as a retriever to fetch relevant documents based on user queries.

## Usage

The notebook provides a practical example of retrieving information about specific topics like the "Greedy Algorithm" from a loaded PDF or Wikipedia page.

```python
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
result = retriever.invoke("Explain greedy algorithm in detail")
```
