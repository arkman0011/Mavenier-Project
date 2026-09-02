"""Step 1 of 3: build the dataset.

Turn the 3GPP spec folders in ``input/3gpp/marked`` into one enriched JSONL
file in ``outputs/enriched_chunks.jsonl``. This is plain text preprocessing:
no embeddings, no Qdrant, no Gemini. Run it once (or again whenever the input
specs change), then run ``scripts.run_ingestion`` to load the JSONL into Qdrant.

    python -m scripts.build_dataset
"""

from pathlib import Path

from mavenier.preprocessing.pipeline import process_corpus

PROJECT_FOLDER = Path(__file__).resolve().parents[1]
CORPUS_ROOT = PROJECT_FOLDER / "input" / "3gpp" / "marked"
OUTPUT_FILE = PROJECT_FOLDER / "outputs" / "enriched_chunks.jsonl"


try:
    number_of_chunks = process_corpus(
        corpus_root=CORPUS_ROOT,
        output_path=OUTPUT_FILE,
        max_tokens=400,
    )
    print("Dataset built successfully!")
    print(f"Chunks written: {number_of_chunks}")
    print(f"Output file: {OUTPUT_FILE}")
    print("Next step: python -m scripts.run_ingestion")
except Exception as error:
    print("Building the dataset failed:")
    print(error)
