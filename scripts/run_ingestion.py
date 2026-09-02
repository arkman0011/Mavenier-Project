"""Step 2 of 3: ingest the dataset.

Embed the chunks in ``outputs/enriched_chunks.jsonl`` and store them in the
local Qdrant database. This step only reads the JSONL; it never rebuilds it.
If the JSONL is missing, build it first with ``scripts.build_dataset``.

    python -m scripts.build_dataset   # step 1, if not done yet
    python -m scripts.run_ingestion   # step 2
"""

from pathlib import Path

from mavenier.rag.retrieval.pipeline import ingest_jsonl

PROJECT_FOLDER = Path(__file__).resolve().parents[1]
CHUNK_FILE = PROJECT_FOLDER / "outputs" / "enriched_chunks.jsonl"
QDRANT_FOLDER = PROJECT_FOLDER / "qdrant_data"


if not CHUNK_FILE.exists():
    print(f"No dataset found at {CHUNK_FILE}.")
    print("Build it first with: python -m scripts.build_dataset")
else:
    try:
        print("Loading BGE-small on CPU and embedding the chunks...")
        summary = ingest_jsonl(CHUNK_FILE, QDRANT_FOLDER)
        print("Ingestion completed successfully!")
        print(f"Chunks stored: {summary['chunks_stored']}")
        print(f"Collection: {summary['collection']}")
        print(f"Qdrant data: {summary['qdrant_path']}")
    except Exception as error:
        print("Ingestion failed:")
        print(error)
