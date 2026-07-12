<div align="center">

# 📄 Document Question Answering System

### A fully local, privacy-first RAG pipeline — no API keys, no cloud, no data leaks.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-🦜-1C3C3C?style=for-the-badge)](https://langchain.com)
[![Ollama](https://img.shields.io/badge/Ollama-Llama%203-black?style=for-the-badge&logo=meta&logoColor=white)](https://ollama.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-FF6B6B?style=for-the-badge)](https://trychroma.com)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)

</div>

---

## 🧠 What is this?

This project implements a **Retrieval-Augmented Generation (RAG)** system that lets you **ask natural language questions directly against your own PDF documents** — all running **100% locally** on your machine.

No OpenAI. No internet. No subscriptions. Just your documents and a local LLM.

> **Built as part of Week 7 of the Data Science program by [Coding Temple](https://www.codingtemple.com/).**

---

## ✨ Key Features

| Feature | Details |
|---|---|
| 🔒 **Fully Local** | Runs entirely on your machine — zero data leaves your system |
| 📑 **Multi-Document Support** | Ingests multiple PDFs and TXT files simultaneously |
| ⚡ **Semantic Search** | `all-MiniLM-L6-v2` embeddings for fast, accurate retrieval |
| 🧩 **Smart Chunking** | `RecursiveCharacterTextSplitter` with 1000-char chunks & 200-char overlap |
| 💾 **Persistent Vector Store** | ChromaDB stores embeddings so you don't re-process on every run |
| 🦙 **Llama 3 via Ollama** | Powerful open-source LLM answering grounded in your documents |
| 📍 **Source Citations** | Every answer includes the exact document chunks used |
| 📊 **System Metrics** | Built-in pipeline report: chunk stats, embedding dims, model info |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR DOCUMENTS (data/)                    │
│              PDFs  ·  TXT files  ·  Any format              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   STEP 1: DATA INGESTION                     │
│     PyPDFLoader / TextLoader → RecursiveCharacterSplitter    │
│          chunk_size=1000  ·  chunk_overlap=200               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                STEP 2: EMBEDDING + STORAGE                   │
│        HuggingFace all-MiniLM-L6-v2 → ChromaDB              │
│               Persistent vector store on disk                │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  STEP 3: RAG QUERY CHAIN                     │
│   User Question → Semantic Retrieval → Llama 3 (Ollama)     │
│      Strict prompt: answers ONLY from retrieved context      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
              ✅  Grounded Answer + Source Citations
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **LLM** | [Llama 3](https://ollama.com/library/llama3) via [Ollama](https://ollama.com) |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` (HuggingFace) |
| **Vector Store** | [ChromaDB](https://www.trychroma.com/) |
| **Orchestration** | [LangChain](https://www.langchain.com/) |
| **PDF Parsing** | [PyPDF](https://pypdf.readthedocs.io/) |
| **Interface** | Jupyter Notebook |

---

## 📁 Project Structure

```
📦 Document-Question-Answering-System
├── 📓 week7_NipunJain.ipynb   # Main notebook — full RAG pipeline
├── 📋 requirements.txt         # Python dependencies
├── 🚫 .gitignore               # Excludes cache, DB, and data files
├── 🛠️ add_explanation_cell.py  # Utility: add markdown cells to notebook
├── 🛠️ fix_nb.py                # Utility: notebook repair script
├── 🛠️ update_nb.py             # Utility: notebook update script
├── 📂 data/                    # ← Place your PDFs/TXTs here (gitignored)
│   ├── Artificial Intelligence.pdf
│   ├── OOP_book.pdf
│   └── database-concepts.pdf
└── 📂 chroma_db/               # ← Auto-generated vector store (gitignored)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/download) installed and running
- Llama 3 model pulled locally

### 1. Clone the Repository

```bash
git clone https://github.com/Nipunjain17/Document-Question-Answering-System.git
cd Document-Question-Answering-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Pull the Llama 3 Model

```bash
ollama pull llama3
```

> Make sure Ollama is running in the background (`ollama serve`)

### 4. Add Your Documents

```bash
mkdir data
# Copy your PDF or TXT files into the data/ folder
```

### 5. Run the Notebook

```bash
jupyter notebook week7_NipunJain.ipynb
```

Run all cells in order — the pipeline will:
1. Load & chunk your documents
2. Embed and store them in ChromaDB
3. Set up the RAG query chain
4. Answer your questions with source citations

---

## 💬 Example Usage

```python
# Ask any question about your documents
response = rag_chain.invoke({"input": "What is Object-Oriented Programming?"})

print(response["answer"])
# → "Object-Oriented Programming is a paradigm that organizes software design
#    around data, or objects, rather than functions and logic..."

print(response["context"])
# → [Source: OOP_book.pdf, Page 12, Chunk 0]
# → [Source: OOP_book.pdf, Page 13, Chunk 1]
```

---

## 📊 Pipeline Configuration

| Parameter | Value |
|---|---|
| Chunk Size | 1,000 characters |
| Chunk Overlap | 200 characters |
| Embedding Model | `all-MiniLM-L6-v2` |
| Embedding Dimensions | 384 |
| LLM | Llama 3 (local via Ollama) |
| Retriever Top-K | 5 chunks |
| Vector DB | ChromaDB (persistent) |

---

## ⚠️ Important Notes

- The `data/` folder and `chroma_db/` are excluded from version control (see `.gitignore`). Add your own PDF/TXT files locally.
- The first run will download the `all-MiniLM-L6-v2` embedding model from HuggingFace (~90MB).
- Ollama must be running locally before executing the notebook.

---

## 👤 Author

**Nipun Jain**  
Data Science Student @ [Coding Temple](https://www.codingtemple.com/)

[![GitHub](https://img.shields.io/badge/GitHub-Nipunjain17-181717?style=flat-square&logo=github)](https://github.com/Nipunjain17)

---

<div align="center">

Made with ❤️ and 🦙 Llama 3

</div>
