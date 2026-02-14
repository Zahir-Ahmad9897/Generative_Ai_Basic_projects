# LangChain Learning Project

A hands-on learning project exploring LangChain framework for building LLM-powered applications. This repository documents practical implementations of core LangChain concepts including chat models, output parsers, document loaders, and API deployment.

## What I Built

This project demonstrates working implementations of LangChain components integrated with multiple L LM providers (Groq, OpenAI, HuggingFace). Each module contains practical examples solving real problems and learning through hands-on coding.

## Project Structure

```
├── 01_basics/              # LangChain fundamentals and API deployment
├── 02_chat_models/         # Multi-provider chat model integration  
├── 03_output_parsers/      # Structured output extraction
├── 04_data_ingestion/      # Document loading from multiple sources
├── 05_embeddings/          # Vector embeddings (in progress)
├── examples/               # Additional standalone examples
└── requirements.txt        # Project dependencies
```

## Technologies

- **LangChain** - Framework for LLM applications
- **Groq** - Fast LLM inference (primary provider)
- **OpenAI** - GPT models integration
- **HuggingFace** - Open-source models (Intel neural-chat-7b)
- **Fas tAPI + LangServe** - API deployment
- **Python 3.12** - Programming language

## What I Learned

### 01_basics - Foundation
- Built my first LangChain chains with Groq's Llama 3.1
- Implemented SystemMessage and HumanMessage for chat conversations
- Created FastAPI server with LangServe to deploy LLM chains as REST APIs
- Learned proper environment variable management for API keys

### 02_chat_models - Multi-Provider Integration
- Integrated HuggingFace's Intel neural-chat-7b-v3-1 model
- Implemented ChatPromptTemplate for dynamic prompts
- Built translation and explanation chains
- Compared different LLM providers and their performance

### 03_output_parsers - Structured Data
- Implemented `StrOutputParser` for clean text extraction
- Mastered `JsonOutputParser` to get raw JSON objects directly from the LLM
- Implemented `StructuredOutputParser` with `ResponseSchema` for multi-field data extraction
- Learned the importance of injecting format instructions into prompts using `partial_variables`
- Successfully built chains that return typed dictionaries (e.g., extracting person details: name, age, gender)
- Debugged and solved common parsing errors (e.g., "unhashable type" and missing format instructions)

### 04_data_ingestion - Document Processing
- Loaded PDFs using PyPDFLoader with metadata extraction
- Implemented CSVLoader for tabular data
- Built WebBaseLoader with BeautifulSoup for web scraping
- Created JSONLoader for structured data ingestion
- Learned how different loaders handle metadata differently

## Key Implementations

### FastAPI Server (01_basics/serve.py)
Deployed a LangChain chain as a REST API endpoint that generates summaries on any topic.

```python
# Chain: Prompt → Groq LLM → String Parser
chain = prompt | llm | output_parser

# Deploy as API
add_routes(app, chain, path="/joke")
```

### HuggingFace Integration (02_chat_models)
Successfully integrated open-source models from HuggingFace with proper tokenizer configuration.

### Document Ingestion Pipeline (04_data_ingestion)
Built a complete pipeline loading PDF (28 pages on AI search algorithms), CSV files, JSON data, and web content.

## Installation

```bash
# Clone repository
git clone <repository-url>
cd Gen\ AI_LANGChain

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env and add your API keys
```

## Usage

### Run Jupyter Notebooks
```bash
jupyter notebook
# Navigate to desired notebook and execute cells
```

### Run FastAPI Server
```bash
cd 01_basics
uvicorn serve:app --reload
# Visit http://localhost:8000/docs for API documentation
```

## Real Examples

All notebooks contain working code with actual outputs from LLM responses. No placeholders - everything has been tested and executed.

## Challenges Solved

-  **Output Parser Errors**: Learned that format instructions MUST be in the prompt, not just attached to the parser
- **HuggingFace Integration**: Configured tokenizers correctly for Intel neural-chat model
- **Web Scraping**: Used BeautifulSoup selectors to extract specific content from documentation pages
- **API Deployment**: Successfully deployed LangChain chains as production-ready REST APIs

## Next Steps

- Implement RAG (Retrieval-Augmented Generation) with vector databases
- Add text splitting and chunking strategies
- Build a complete QA system over documents
- Explore agent-based systems with tool usage

## References

- [LangChain Documentation](https://python.langchain.com/)
- [Groq API](https://console.groq.com/)
- [HuggingFace Models](https://huggingface.co/models)

---

This project represents active learning and experimentation with cutting-edge LLM technology. Each implementation solved real problems and taught practical skills for building AI-powered applications.
