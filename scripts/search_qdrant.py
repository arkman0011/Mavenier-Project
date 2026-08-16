"""Beginner entry point for interactive semantic search."""

from pathlib import Path

from mavenier.rag.retrieval.pipeline import search_text

PROJECT_FOLDER = Path(__file__).resolve().parents[1]
QDRANT_FOLDER = PROJECT_FOLDER / "qdrant_data"


try:
    query = input("Enter your 3GPP question: ").strip()
    results = search_text(query, qdrant_path=QDRANT_FOLDER, limit=5)
    if not results:
        print("No matching chunks were found.")
    for number, result in enumerate(results, start=1):
        print(f"\nResult {number} | score={result['score']:.4f}")
        print(f"Source: {result['source']}")
        print(f"Section: {result['section']}")
        print(result["text"])
except Exception as error:
    print("Search failed:")
    print(error)

