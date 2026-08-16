"""Beginner entry point: preprocess if needed, then embed and store chunks."""

from pathlib import Path

from mavenier.rag.ingestion.pipeline import process_markdown
from mavenier.rag.retrieval.pipeline import ingest_jsonl

PROJECT_FOLDER = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FOLDER / "input" / "MD Combined.md"
CHUNK_FILE = PROJECT_FOLDER / "outputs" / "enriched_chunks.jsonl"
QDRANT_FOLDER = PROJECT_FOLDER / "qdrant_data"


try:
    if not CHUNK_FILE.exists():
        print("No JSONL file found, so preprocessing will run first.")
        process_markdown(INPUT_FILE, CHUNK_FILE, max_tokens=400)

    print("Loading BGE-small on CPU and embedding the chunks...")
    summary = ingest_jsonl(CHUNK_FILE, QDRANT_FOLDER)
    print("Ingestion completed successfully!")
    print(f"Chunks stored: {summary['chunks_stored']}")
    print(f"Collection: {summary['collection']}")
    print(f"Qdrant data: {summary['qdrant_path']}")
except Exception as error:
    print("Ingestion failed:")
    print(error)

