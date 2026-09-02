"""Tests for path- and header-derived document metadata (no Docling needed)."""

import pytest

from mavenier.preprocessing.loader import (
    discover_markdown_documents,
    parse_document_header,
    parse_document_path,
)


def test_parse_document_path_extracts_release_series_and_spec():
    metadata = parse_document_path(
        "/data/input/3gpp/marked/Rel-11/36_series/36106/raw.md"
    )
    assert metadata["release"] == "Rel-11"
    assert metadata["release_number"] == 11
    assert metadata["series"] == "36"
    assert metadata["spec_number"] == "36106"
    assert metadata["document_id"] == "TS 36.106"


def test_parse_document_path_handles_two_digit_release():
    metadata = parse_document_path(
        "/x/marked/Rel-20/22_series/22261/raw.md"
    )
    assert metadata["release"] == "Rel-20"
    assert metadata["release_number"] == 20
    assert metadata["series"] == "22"
    assert metadata["document_id"] == "TS 22.261"


def test_parse_document_path_relative_path_against_root():
    metadata = parse_document_path(
        "/x/marked/Rel-20/32_series/32160/raw.md",
        corpus_root="/x/marked",
    )
    assert metadata["relative_path"] == "Rel-20/32_series/32160/raw.md"


def test_parse_document_path_ignores_unrecognised_layout():
    metadata = parse_document_path("/somewhere/notes/raw.md")
    assert "release" not in metadata
    assert "series" not in metadata
    assert "document_id" not in metadata


def test_parse_document_header_reads_version_and_date():
    header = "# 3GPP TS 22.261 V20.5.0 (2025-12)\n\n*Technical Specification*\n"
    metadata = parse_document_header(header)
    assert metadata["version"] == "V20.5.0"
    assert metadata["date"] == "2025-12"
    assert metadata["year"] == 2025
    assert metadata["document_id"] == "TS 22.261"


def test_parse_document_header_absent_fields_are_omitted():
    metadata = parse_document_header("# Contents\n\n| Foreword | 5 |\n")
    assert metadata == {}


def test_discover_markdown_documents_sorted(tmp_path):
    first = tmp_path / "Rel-11" / "23_series" / "23002"
    second = tmp_path / "Rel-20" / "22_series" / "22261"
    for folder in (second, first):  # created out of order on purpose
        folder.mkdir(parents=True)
        (folder / "raw.md").write_text("# doc", encoding="utf-8")

    found = discover_markdown_documents(tmp_path)
    assert [path.parent.name for path in found] == ["23002", "22261"]


def test_discover_markdown_documents_requires_existing_files(tmp_path):
    with pytest.raises(FileNotFoundError):
        discover_markdown_documents(tmp_path)
