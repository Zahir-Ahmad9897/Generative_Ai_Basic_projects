# Generative AI Development with LangChain

This repository contains a comprehensive collection of implementations focused on building enterprise-grade LLM applications using the LangChain framework. The project demonstrates the integration of multiple model providers, structured data extraction, and robust data ingestion pipelines.

## Project Structure

*   **01_basics**: Foundation of LangChain operations and API deployment using LangServe.
*   **02_chat_models**: Integration of diverse LLM providers including Groq, OpenAI, and Hugging Face.
*   **03_output_parsers**: Advanced techniques for extracting structured data and validating model responses.
*   **04_data_ingestion**: Scalable document processing from PDF, CSV, JSON, and web sources.
*   **05_embeddings**: Vector-based data representation and retrieval strategies.

## Technical Stack

*   **Framework**: LangChain
*   **Model Providers**: Groq (Llama), OpenAI (GPT), Hugging Face (Open Source)
*   **Deployment**: FastAPI, LangServe, Uvicorn
*   **Environment**: Python 3.12, Pydantic, Dotenv

## Core Modules

### Structured Output Extraction
Focused on converting natural language into actionable data.
*   **PydanticOutputParser**: Direct conversion of LLM responses into validated Python objects.
*   **StructuredOutputParser**: Schema-based extraction utilizing ResponseSchema for complex multi-field data.
*   **JsonOutputParser**: Reliable JSON formatting for downstream API consumption.
*   **StrOutputParser**: Streamlined text processing and metadata removal.

### Data Ingestion and Processing
Robust pipeline for ingesting unstructured data sources.
*   **PDF Processing**: Metadata-aware extraction from technical documentation.
*   **Web Scraping**: Integration with BeautifulSoup for targeted content retrieval.
*   **Structured Formats**: Efficient ingestion of CSV and JSON datasets.

### API Deployment
Production-ready deployment of LangChain chains as RESTful endpoints via FastAPI and LangServe, enabling seamless integration with external applications.

## Installation

1.  **Clone Repository**
    ```bash
    git clone [repository-url]
    cd Gen_AI_LANGChain
    ```

2.  **Environment Setup**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    ```

3.  **Dependency Installation**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration**
    Initialize `.env` with required API keys for Groq, OpenAI, and Hugging Face.

## Usage

*   **Development**: Access the implementation details via Jupyter Notebooks for interactive testing.
*   **Production**: Deploy the API server using `uvicorn serve:app --reload` within the relevant module directory.

