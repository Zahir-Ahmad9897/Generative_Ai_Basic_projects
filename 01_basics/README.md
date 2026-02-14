# LangChain Basics

First steps with LangChain - building chat chains and deploying them as APIs.

## What's In Here

**LangchainB1.ipynb** - My first LangChain implementation
- Connected to Groq's Llama 3.1-8b model
- Created chat conversations with SystemMessage and HumanMessage
- Asked the LLM  "What are the top 2 benefits of using langchain?"
- Got a detailed response about unified interfaces and improved scalability

**LangchainB2_Loader.ipynb** - Loading different document types
- TextLoader: Read .txt files
- PyPDFLoader: Extracted text from PDF with metadata (producer, creator, page numbers)
- WebBaseLoader: Scraped LangChain documentation with BeautifulSoup
- Learned about document metadata structure

**serve.py** - REST API deployment
- Built a FastAPI server using LangServe
- Created a chain: `ChatPromptTemplate | ChatGroq | StrOutputParser`
- Deployed it as `/joke` endpoint
- Can now call LLM through HTTP requests

## What I Learned

1. **LangChain chains use the pipe operator** (`|`) to connect components
2. **Groq is FAST** - responses come back almost instantly
3. **LangServe makes deployment simple** - just `add_routes(app, chain, path="/endpoint")`
4. **Environment variables are critical** - never hardcode API keys

## Running the Code

```bash
# Notebooks
jupyter notebook LangchainB1.ipynb

# API Server
python serve.py
# OR
uvicorn serve:app --reload
```

Visit `http://localhost:8000/docs` to see interactive API documentation.

## Actual Output Example

From LangchainB1.ipynb when asking about LangChain benefits:
```
1. Unified Interface for Multiple AI Models: LangChain provides a unified interface 
   for integrating multiple AI models and interfaces...
   
2. Improved Efficiency and Scalability: LangChain's architecture enables developers 
   to build more efficient and scalable AI models...
```

This was my introduction to how LangChain structures responses and handles different LLM providers.
