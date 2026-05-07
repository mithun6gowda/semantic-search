# Semantic Search Engine

A production-style Semantic Search Engine built using **FastAPI**, **Qdrant**, **OpenAI Embeddings**, and **Cross-Encoder Reranking**.

The system supports ingestion from both **PDF documents** and **web URLs**, converts them into vector embeddings, and performs semantic retrieval over health-related content.

This project was built to understand how modern retrieval systems work internally — including vector search, chunking strategies, reranking pipelines, and scalable ingestion workflows.

---

#  Features

- Semantic search using dense embeddings
- Vector similarity search with Qdrant
- Cross-encoder reranking for improved relevance
- PDF ingestion pipeline
- Web URL ingestion pipeline
- Metadata-aware storage (`pdf` / `web`)
- FastAPI REST API
- Chunk-based retrieval
- Production-style modular architecture

---

#  Architecture

```text
PDFs / URLs
      │
      ▼
Text Extraction
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
(OpenAI Embeddings)
      │
      ▼
Qdrant Vector DB
      │
      ▼
Semantic Retrieval
      │
      ▼
Cross-Encoder Reranking
      │
      ▼
FastAPI Search API
```

---

#  Tech Stack

| Component | Technology |
|---|---|
| Backend API | FastAPI |
| Vector Database | Qdrant |
| Embeddings | OpenAI Embeddings |
| Reranking | Sentence Transformers CrossEncoder |
| PDF Parsing | PyMuPDF |
| Web Scraping | BeautifulSoup |
| Language | Python |

---

# 📂 Project Structure

```text
semantic-search/
│
├── app/
│   ├── config.py
│   ├── embedding.py
│   ├── main.py
│   ├── pdf_loader.py
│   ├── reranker.py
│   ├── search.py
│   ├── vector_db.py
│   └── web_loader.py
│
├── scripts/
│   └── ingest.py
│
├── data/
│   └── pdfs/
│
├── requirements.txt
└── README.md
```

#  Setup

## 1. Clone Repository

```bash
git clone https://github.com/mithun6gowda/semantic-search.git

cd semantic-search
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# 🐳 Start Qdrant

Run Qdrant locally using Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

Verify Qdrant is running:

```text
http://localhost:6333/dashboard
```

---

# 📥 Data Ingestion

The system supports two ingestion sources:

---

## 1. PDF Ingestion

Place PDFs inside:

```text
data/pdfs/
```

Then run:

```bash
python -m scripts.ingest
```

---

## 2. Web URL Ingestion

Health-related URLs are configured inside:

```text
scripts/ingest.py
```

Example:

```python
HEALTH_URLS = [
    "https://www.who.int/news-room/fact-sheets/detail/diabetes",
    "https://www.cdc.gov/diabetes/basics/diabetes.html"
]
```

The ingestion pipeline:

- Extracts content
- Chunks text
- Generates embeddings
- Stores vectors in Qdrant

---

# ▶️ Run API Server

```bash
uvicorn app.main --reload
```

Server runs on:

```text
http://127.0.0.1:8000
```

---

# 🔎 Search API

## Example Query

```text
http://127.0.0.1:8000/search?query=diabetes
```

---

## Example Response

```json
{
  "results": [
    {
      "text": "Type 1 diabetes treatment includes taking a medicine called insulin for the rest of your life, and regularly checking your blood glucose (sugar) levels. Type 2 diabetes treatment and gestational diabetes treatment include lifestyle changes such as healthy eating.",
      "score": 0.91
    }
  ]
}
```

---

# 🧠 Retrieval Pipeline

The search flow uses a **two-stage retrieval architecture**.

---

## Stage 1 — Dense Retrieval

- Query embeddings generated using OpenAI
- Similar vectors retrieved from Qdrant

---

## Stage 2 — Cross-Encoder Reranking

Candidate chunks are reranked using:

```text
cross-encoder/ms-marco-MiniLM-L-6-v2
```

This significantly improves ranking precision compared to vector similarity alone.

---

# 📊 Current Capabilities

- Semantic retrieval over health documents
- Multi-source ingestion
- Metadata-aware indexing
- Reranked search results
- Scalable vector-based architecture

---

# ⚡ Future Improvements

Planned upgrades include:

- Hybrid Search (BM25 + Vector Search)
- Redis caching
- Query expansion
- Semantic chunking
- Evaluation metrics (Recall@K, NDCG)
- Docker Compose setup
- Kubernetes deployment
- Streaming ingestion pipeline

---

# 🧪 Example Queries

Try searching:

- `diabetes symptoms`
- `blood glucose levels`
- `heart disease causes`

---

# 🧠 Learnings From This Project

Key engineering learnings while building this project:

- Retrieval quality depends heavily on chunking strategy
- Reranking dramatically improves semantic relevance
- Data ingestion pipelines fail more often than models
- Metadata becomes critical as datasets grow
- Vector search alone is not enough for production-grade retrieval

---

# 📌 References

Helpful resources used while learning:

- Qdrant Documentation
- FastAPI Documentation
- Sentence Transformers
- OpenAI Embeddings Guide
- Semantic search architecture examples and related open-source projects

---

# 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

Feel free to:

- Open issues
- Create pull requests
- Improve retrieval quality
- Add new ingestion pipelines