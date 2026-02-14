# Data Ingestion

Loading documents from different sources into LangChain format.

## What I Built

**Data_ingestion_1.ipynb** - Multi-format document loading

Implemented 4 different document loaders:

### 1. PyPDFLoader - PDF Documents
Loaded a 28-page PDF lecture on AI search algorithms (Lecture03.pdf)

What I extracted:
- Page content from all 28 pages
- Metadata: producer, creator, creation date, author, page numbers
- Topics covered: BFS, DFS, Hill Climbing, Heuristic Search

Example metadata from page 1:
```python
{
    'producer': 'Microsoft® PowerPoint® LTSC',
    'author': 'Athar Sethi',
    'total_pages': 28,
    'page': 0,
    'page_label': '1'
}
```

### 2. CSVLoader - Tabular Data
Loaded CSV file with student data

Learned that CSVLoader:
- Converts each row to a Document
- Preserves column names
- Can access individual rows: `data[9].page_content`

### 3. WebBaseLoader - Web Scraping
Scraped LangChain documentation using BeautifulSoup

```python
loader = WebBaseLoader(
    web_paths=("https://docs.langchain.com/...),
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(id=("content")))
)
```

Successfully extracted documentation content about document loaders (meta!).

### 4. JSONLoader - Structured Data
Loaded JSON from a REST API

```python
# Fetched data from API
response = requests.get(url)

# Saved and loaded with JSONLoader
loader = JSONLoader(
    file_path="temp.json",
    jq_schema=".",
    text_content=False
)
```

Extracted posts, comments, and profile data from JSON structure.

## Key Learnings

**Every loader returns Documents** - Same format regardless of source:
```python
Document(
    page_content="...",  # The actual text
    metadata={...}        # Source info
)
```

**Metadata varies by loader:**
- PDF: pages, author, dates
- CSV: row info
- Web: URL, scrape time
- JSON: file path, sequence number

**BeautifulSoup integration** - Can target specific HTML elements:
- Use `SoupStrainer` to extract only relevant parts
- Reduces noise from headers/footers/navigation

**Web scraping note** - Attempted to use requests-html for JavaScript rendering but hit Chromium download issues. Learned that WebBaseLoader is simpler for static content.

## Practical Applications

This work prepares for:
- Building RAG (Retrieval Augmented Generation) systems
- Processing knowledge bases
- Creating searchable document repositories
- Feeding varied data sources into LLM applications

## Actual Data Loaded

- **PDF**: 28 pages of AI algorithms lecture
- **CSV**: Student PLO chart data
- **Web**: LangChain integration documentation  
- **JSON**: Social media API data (posts/comments)

All successfully converted to LangChain Document format for downstream processing.

## Next Steps

This document loading is the first step. Next would be:
- Text splitting for chunk management
- Embedding generation
- Vector store integration
- Building retrieval systems
