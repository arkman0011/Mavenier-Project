"""FastAPI layer that prepares Qdrant automatically on first startup."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Annotated, Any

from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel, Field

from mavenier.rag.pipeline import ask_agentic_rag
from mavenier.rag.retrieval.pipeline import ingest_jsonl
from mavenier.rag.retrieval.vector_store import COLLECTION_NAME, get_qdrant_client

LOGGER = logging.getLogger(__name__)

# Qdrant exact-match filters accept scalar values or lists of scalar values.
# Restricting the type here prevents Swagger's old `{}` placeholder from being
# sent to Qdrant as an invalid MatchValue.
FilterScalar = str | int | bool
FilterValue = FilterScalar | list[FilterScalar]

# All paths are based on this file, so the command works from any terminal folder.
PROJECT_FOLDER = Path(__file__).resolve().parents[2]
CHUNK_FILE = PROJECT_FOLDER / "outputs" / "enriched_chunks.jsonl"
QDRANT_FOLDER = PROJECT_FOLDER / "qdrant_data"


def collection_is_ready() -> bool:
    """Return True only when the local collection exists and contains chunks."""
    client = get_qdrant_client(QDRANT_FOLDER)
    try:
        if not client.collection_exists(COLLECTION_NAME):
            return False
        collection = client.get_collection(COLLECTION_NAME)
        return int(getattr(collection, "points_count", 0) or 0) > 0
    finally:
        close = getattr(client, "close", None)
        if callable(close):
            close()


def prepare_knowledge_base() -> None:
    """Load the prepared dataset into Qdrant if it is not already loaded.

    The dataset (``outputs/enriched_chunks.jsonl``) ships as part of the repo,
    built offline by ``scripts.build_dataset``. The API only ever ingests it.
    """
    if collection_is_ready():
        LOGGER.info(
            "Qdrant collection %r is ready; ingestion skipped.", COLLECTION_NAME
        )
        return

    LOGGER.info(
        "Preparing Qdrant collection %r. First startup may take time.", COLLECTION_NAME
    )
    summary = ingest_jsonl(CHUNK_FILE, QDRANT_FOLDER, COLLECTION_NAME)
    LOGGER.info("Knowledge base ready: %s chunks stored.", summary["chunks_stored"])


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Prepare the knowledge base before accepting the first API request."""
    prepare_knowledge_base()
    yield


app = FastAPI(
    title="3GPP Telecom RAG API",
    description="Agentic LangGraph answers using the existing BGE, Qdrant, reranker, and Gemini services.",
    version="2.0.0",
    lifespan=lifespan,
)


class AskRequest(BaseModel):
    """JSON body accepted by POST /ask."""

    question: str = Field(min_length=1, max_length=2000)
    filters: dict[str, FilterValue] | None = None
    debug: bool = False


class AskResponse(BaseModel):
    """Grounded result plus transparent confidence and citations."""

    answer: str
    confidence: float = Field(ge=0.0, le=1.0)
    sources: list[dict[str, str | None]] = Field(default_factory=list)
    debug: dict[str, Any] | None = None


@app.get("/")
def service_information() -> dict[str, str]:
    """Provide a useful landing response instead of an unexplained 404."""
    return {
        "name": "3GPP Telecom RAG API",
        "status": "ok",
        "documentation": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    """Confirm that the API process is running without loading AI models."""
    return {"status": "ok"}


def _http_status_for_error(message: str) -> int:
    """Map known query-time failures to beginner-friendly HTTP statuses."""
    lowered = message.lower()
    if "rate limit" in lowered or "quota" in lowered:
        return 429
    if any(
        phrase in lowered
        for phrase in (
            "missing",
            "not installed",
            "does not exist",
            "could not load",
            "authentication failed",
            "network or api error",
            "qdrant",
        )
    ):
        return 503
    return 500


@app.post("/ask", response_model=AskResponse)
def ask_question(
    request: Annotated[
        AskRequest,
        Body(
            openapi_examples={
                "question_without_filters": {
                    "summary": "Ask a normal question",
                    "value": {
                        "question": "What should the eNodeB do when an S1-AP path failure is detected?",
                        "filters": None,
                        "debug": False,
                    },
                },
                "question_with_timer_filter": {
                    "summary": "Ask with an optional timer filter",
                    "value": {
                        "question": "What happens when T300 expires?",
                        "filters": {"timer.timer_name": "T300"},
                        "debug": False,
                    },
                },
            }
        ),
    ],
) -> AskResponse:
    """Run the explicit LangGraph workflow over the existing query services."""
    try:
        result = ask_agentic_rag(
            question=request.question,
            filters=request.filters,
            debug=request.debug,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        message = str(exc)
        raise HTTPException(
            status_code=_http_status_for_error(message),
            detail=message,
        ) from exc
    return AskResponse(**result)
