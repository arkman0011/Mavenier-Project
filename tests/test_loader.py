from mavenier.rag.ingestion.loader import extract_markdown_headings, find_section_for_chunk, split_combined_markdown


def test_splits_source_file_markers():
    text = """<!-- ===== SOURCE FILE: first.md ===== -->
# First
Text one.
<!-- ===== SOURCE FILE: second.md ===== -->
# Second
Text two.
"""
    assert split_combined_markdown(text, "combined.md") == [
        ("first.md", "# First\nText one."),
        ("second.md", "# Second\nText two."),
    ]


def test_normal_markdown_is_one_section():
    assert split_combined_markdown("# Title\nText", "one.md") == [
        ("one.md", "# Title\nText")
    ]


def test_heading_hierarchy_and_nearest_section():
    text = """# 5 RRC procedures
## 5.3 Connection control
### 5.3.3 RRC connection establishment

The UE shall start timer T300.
"""
    headings = extract_markdown_headings(text)
    matched = find_section_for_chunk("The UE shall start timer T300.", headings)
    assert matched is not None
    assert matched.title == "5.3.3 RRC connection establishment"
    assert matched.path == [
        "5 RRC procedures",
        "5.3 Connection control",
        "5.3.3 RRC connection establishment",
    ]

