# RAG‑Scout 📡🧭  
**_A LangChain‑powered benchmark harness that scouts every retriever path and crowns the best stack for your Retrieval‑Augmented‑Generation workload._**

---

## 1 · Why RAG‑Scout?

| Pain‑point | Typical reality | RAG‑Scout fix |
|------------|-----------------|---------------|
| _“Which embedding model and vector DB should we deploy?”_ | Ad‑hoc A/B tests; days of manual wiring. | YAML grid → one command → ranked leaderboard. |
| _“OpenAI, Cohere, Voyage, MiniLM, E5… I’ve lost count.”_ | Each new model needs a fresh script. | LangChain adapters auto‑wire **all** embeddings. |
| _“Vector DB latency vs BM25 accuracy? We guess.”_ | Teams stick with defaults (FAISS‑flat) and hope. | RAG‑Scout times every query and reports recall + latency |

---

## 2 · What is it?

**RAG‑Scout** is a Python tool that:

1. **Loads any dataset** split into a `corpus.txt` and a `qa.tsv` (or BEIR JSONL).  
2. **Composes every combination** of  
   * **Similarity method (A)** – dense (vector), sparse (BM25 / SPLADE), hybrid (RRF, α‑fusion), rerankers.  
   * **Vector backend (B)** – every store LangChain supports today (FAISS, HNSWlib, Chroma, Pinecone, Weaviate, Qdrant, Milvus, Vespa, Elastic + KNN, pgvector, Redis‑Vector …).  
   * **Embedding model (C)** – via LangChain’s `Embeddings` API: OpenAI `text‑embedding‑4`, Cohere v3, Voyage‑3, HuggingFace models (MiniLM, GTR, E5, Stella, Instructor, domain‑specific BioBERT/SciBERT), plus whatever drops tomorrow.  
   _→ A × B × C matrix, automatically._  
3. Indexes, queries, and **computes IR metrics** (nDCG@k, Recall@k, MRR, EM@k) ± std over repeats.  
4. Logs **latency and per‑query cost** (uses LangChain’s `CallbackManager` to capture timing and token usage).  
5. Emits a **Markdown + HTML report** with an emoji trophy on the true winner for your data.

One CLI:  

```bash
ragscout run configs/full_bench.yaml --dataset data/my_corpus
```

---

## 3 · Project goals

* **Zero‑hassle experimentation** – change YAML, not Python.  
* **Breadth over bias** – include _every_ model / backend LangChain exposes; no hidden favourites.  
* **Reproducible** – single `results/*.json` per run with corpus hash, Git hash, dependency versions, env keys (redacted).  
* **Extensible** – add a new backend in `embeddings.py` or `backends.py`, register it once, gain full grid coverage.  
* **Actionable** – latency and token‑bill numbers sit next to nDCG, so “best” means *best fit*, not just highest score.

---

## 4 · Who should use it?

* **LLM / ML engineers** validating RAG stacks before production.  
* **Data scientists** choosing between on‑prem FAISS versus managed Pinecone.  
* **Solution architects / consultants** benchmarking vendor APIs for clients.  
* **Researchers** comparing retrieval paradigms under identical conditions.

If you simply want a working chatbot, you don’t need RAG‑Scout.  
If you must prove _why_ backend X with embedding Y beats Z by **24 % Recall@10 at half the latency**, RAG‑Scout is your scout.

---

## 5 · Features 🔑

| Category | Details |
|----------|---------|
| **LangChain‑native** | All embeddings via `langchain.embeddings.*` and all vector stores via `langchain.vectorstores.*`. You inherit every new model/backend LangChain adds. |
| **Pluggable metrics** | Built‑in IR (nDCG, Recall, MRR, EM) plus optional RAGAS or Open‑RAG‑Eval hooks for answer correctness / hallucination. |
| **Config via YAML** | Grid of runs, repeats, k‑values, metric priority. |
| **.env‑driven** | Single `.env` for OpenAI, Cohere, Pinecone, etc., loaded through `python‑dotenv` in `rag_scout.config`. |
| **Reports** | Markdown table + Jinja2 HTML dashboard (sortable) with latency/cost scatter plots. |
| **Caching** | Disk cache of embeddings so reruns reuse vectors. |
| **CLI & Python API** | `ragscout run …` or programmatic `from rag_scout import Experiment`. |
| **Tested & formatted** | `pytest`, `ruff`, `black`, `mypy` gates in CI. |

---

## 6 · Quickstart

```bash
# 0.  clone & install
pip install -e ".[dev]"

# 1.  copy .env template
cp .env.example .env && nano .env   # add your API keys

# 2.  run the toy grid
python -m rag_scout.run configs/toy.yaml
cat results/summary.md
```

Replace `data/toy` with your real corpus, expand `configs/full_bench.yaml` with any models/backends, re‑run, and read the leaderboard.

---

## 7 · Why the world needs another RAG benchmark?

Existing evals focus on **models** or **databases** in isolation.  
Real‑world retrieval is a **stack**.  
Embedding choice, ANN parameters, fusion weights, and backend latency interact in non‑obvious ways.  
RAG‑Scout treats the whole stack as the unit of comparison—because that’s what your users experience.

---

Happy scouting 🧭