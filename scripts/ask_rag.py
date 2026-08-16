"""Beginner-friendly terminal entry point for the complete RAG system."""

from pathlib import Path

from mavenier.rag.pipeline import ask_agentic_rag

PROJECT_FOLDER = Path(__file__).resolve().parents[1]
QDRANT_FOLDER = PROJECT_FOLDER / "qdrant_data"
DEBUG = True


try:
    question = input("Ask a 3GPP question: ").strip()
    result = ask_agentic_rag(
        question=question,
        qdrant_path=QDRANT_FOLDER,
        debug=DEBUG,
    )
    print("\nAnswer:")
    print(result["answer"])
    print(f"\nConfidence: {result['confidence']:.2f}")
    if result["sources"]:
        print("Sources:")
        for source in result["sources"]:
            print(
                f"- {source['source']} | section={source.get('section') or 'Not provided'}"
            )
    if DEBUG:
        print("\nDebug trace:")
        for entry in result.get("debug", {}).get("trace", []):
            print(entry)
except Exception as error:
    print("\nRAG question failed:")
    print(error)
