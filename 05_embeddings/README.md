# 05 | Text Embeddings & Vector Search

This module focuses on converting text into numerical vectors (Embeddings) and performing semantic similarity searches using **FAISS** and **HuggingFace**.

##  Features Implemented
- **Data Ingestion**: Loading PDF documents using `PyPDFLoader`.
- **Text Splitting**: Utilizing `RecursiveCharacterTextSplitter` to create meaningful document chunks.
- **Open Source Embeddings**: Implementing `BAAI/bge-small-en` from HuggingFace for efficient, local vector generation.
- **Vector Storage**: Using **FAISS** (Facebook AI Similarity Search) for high-performance vector retrieval.

##  Tech Stack
- **LangChain**: Framework for LLM application development.
- **PyTorch (CPU)**: Backend engine for running embedding models locally.
- **FAISS-CPU**: Library for efficient similarity search.
- **HuggingFace Hub**: Source for open-source transformer models.

##  Troubleshooting (Windows Setup)
During development, we resolved several critical environment issues specific to Windows 10/11:

1. **OSError: [WinError 1114]**: 
   - **Cause**: Standard PyTorch attempting to load missing/incompatible CUDA DLLs.
   - **Fix**: Installed the CPU-only version of PyTorch:
     ```powershell
     uv pip install torch --index-url https://download.pytorch.org/whl/cpu
     ```

2. **Access Denied (OS Error 5)**:
   - **Cause**: Attempting to update packages while the Jupyter Kernel is active.
   - **Fix**: Forcefully stopping Python processes before running `uv add`:
     ```powershell
     Stop-Process -Name "python" -Force
     ```

3. **NoneType Version Error**:
   - **Cause**: Corrupted metadata after a failed install.
   - **Fix**: Performed a `--force-reinstall` of affected packages.

##  Project Structure
- `Embedding_Tech.ipynb`: Main notebook containing the splitting and embedding logic.
- `README.md`: Module documentation and troubleshooting guide.
- `faiss_index/`: (Optional) Local storage for the generated vector index.

---
*This module is part of the Generative AI Basic Projects series.*
