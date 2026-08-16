# Agentic query and answer stage

The query-time system is orchestrated by LangGraph while reusing the existing
BGE embedding service, local Qdrant collection, cross-encoder reranker, and
Gemini client. Ingestion and the stored metadata schema are unchanged.

```text
mavenier.rag.pipeline.ask_agentic_rag
  -> mavenier.rag.graph.agentic_rag_graph
  -> mavenier.rag.agents.*
  -> existing retrieval / reranking / Gemini services
```

LangGraph keeps a shared `RAGState`. Each node reads that state and returns only
its updates. Two conditional edges control all retry behavior:

- Insufficient evidence returns to query refinement and retrieval, capped at
  two refinements.
- Unsupported answer claims return to answer regeneration, capped at one
  rewrite.

No-evidence and persistent-verification failures are safe refusal paths. Gemini
errors, Qdrant errors, embedding failures, and reranker failures remain system
errors and are never mislabeled as weak document evidence.

## Ask from the terminal

From the repository root:

```bash
python -m scripts.ask_rag
```

Set `DEBUG` in the script to return a stage trace. The trace includes plans,
scores, sources, decisions, and retry counts, but excludes vectors, API keys,
and hidden model reasoning.

To inspect the workflow as Mermaid text:

```bash
python -m scripts.show_graph
```

## Ask through FastAPI

```bash
python -m uvicorn mavenier.api.app:app --host 127.0.0.1 --port 8000
```

Use `POST /ask` from `http://127.0.0.1:8000/docs`:

```json
{
  "question": "What is an RRC Connection?",
  "filters": null,
  "debug": false
}
```

The response contains `answer`, `confidence`, and `sources`. When `debug` is
true, it also contains structured query analysis, search planning, evidence,
verification, retry counts, and the safe stage trace.
