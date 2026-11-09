"""CR-MET-024 seed/enrichment ownership tests.

The seed-fidelity check (`ingest_seed.py --check`) rebuilds every
seed-derived record from the workbook and demands byte-equality. When
CR-MET-021 attached `external_references` (the managed MAMA
cross-reference relationship) and matching change_history entries to
seed-derived records, that check could never pass again: the rebuilt
record dropped the enrichment. The ruling: those fields are
enrichment-owned, and `merge_enrichment` folds them back into the
rebuilt record. These tests pin the merge and prove the whole corpus
converges.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from ingest_seed import merge_enrichment  # noqa: E402

BASE = Path(__file__).parent.parent


def _built() -> dict:
    return {
        "id": "dea:metric-example",
        "version": "1.1.0",
        "formula_definition": {"expression": "E = a / b"},
        "metadata": {
            "established_by": "CR-MET-016",
            "change_history": [
                {"cr": "CR-MET-016", "date": "2026-10-26", "change": "Ingested"},
                {"cr": "CR-MET-020", "date": "2026-10-26", "change": "Derived fields"},
            ],
        },
    }


def _enriched_on_disk() -> dict:
    record = _built()
    record["external_references"] = [
        {"source": "MAMA", "source_id": "mama-metrics:card/example", "relationship": "broadens"}
    ]
    record["metadata"]["change_history"].append(
        {"cr": "CR-MET-021", "date": "2026-11-04", "change": "Added external_references"}
    )
    return record


def test_external_references_preserved_immediately_before_metadata():
    merged = merge_enrichment(_built(), _enriched_on_disk())
    keys = list(merged)
    assert keys.index("external_references") == keys.index("metadata") - 1, (
        "enrichment must sit immediately before metadata (the CR-MET-021 placement)"
    )
    assert merged["external_references"] == _enriched_on_disk()["external_references"]


def test_enrichment_change_history_entries_appended_verbatim():
    merged = merge_enrichment(_built(), _enriched_on_disk())
    history = merged["metadata"]["change_history"]
    assert history[:2] == _built()["metadata"]["change_history"], "seed entries must stay first"
    assert history[2] == _enriched_on_disk()["metadata"]["change_history"][2]


def test_merge_is_byte_stable_when_reapplied():
    once = merge_enrichment(_built(), _enriched_on_disk())
    twice = merge_enrichment(_built(), once)
    assert twice == once, "merging the merged output again must change nothing"


def test_record_without_enrichment_is_not_mutated():
    plain = _built()
    assert merge_enrichment(_built(), plain) == plain
    assert merge_enrichment(_built(), {}) == _built()


def test_whole_corpus_converges_on_ingest_check():
    """The real gate: `ingest_seed.py --check` exits 0 over all 4,433 records —
    the CR-MET-021 enriched seed records keep their cross-references and every
    other record matches the workbook byte-for-byte."""
    result = subprocess.run(
        [sys.executable, str(BASE / "scripts" / "ingest_seed.py"), "--check"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, f"seed check failed:\n{result.stdout}\n{result.stderr}"
