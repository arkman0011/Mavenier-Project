"""Beginner-friendly file to run by clicking the editor's Run button."""

from pathlib import Path

from mavenier.rag.ingestion.pipeline import process_markdown

# This script expects the Markdown file inside the project's input folder.
PROJECT_FOLDER = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FOLDER / "input" / "MD Combined.md"
OUTPUT_FILE = PROJECT_FOLDER / "outputs" / "enriched_chunks.jsonl"


try:
    number_of_chunks = process_markdown(
        input_path=INPUT_FILE,
        output_path=OUTPUT_FILE,
        max_tokens=400,
    )
    print("Processing completed successfully!")
    print(f"Number of chunks: {number_of_chunks}")
    print(f"Output file: {OUTPUT_FILE}")
except Exception as error:
    print("Processing failed:")
    print(error)

