"""Layout guard for the CR-MET-024 shard level.

The corpus moved from a flat `entities/v1-alpha/<id>/` layout to the
sharded `entities/v1-alpha/<shard>/<id>/` form so no directory ever
reaches GitHub's 1,000-entry listing truncation. These tests pin the
invariants that make that safe permanently:

- every record file sits at exactly the path derived from its id
  (entity-storage-layout.md §5);
- every record directory is complete (`<id>.yaml` + `README.md`);
- `entities/v1-alpha` stays under 27 entries (26 letters + `0-9`) and
  every shard stays below the 800-record trigger that the ratified
  storage contract names (§4);
- CATALOG.yaml paths are the id-derived paths.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

BASE = Path(__file__).parent.parent
SCRIPTS = BASE / "scripts"
sys.path.insert(0, str(SCRIPTS))
from _catalog import ENTITIES_ROOT, record_relpath, shard_for_id  # noqa: E402

# entity-storage-layout.md §4: shard before any directory approaches
# 800 records; GitHub truncates listings at 1,000.
MAX_SHARD_ENTRIES = 800
MAX_ROOT_ENTRIES = 27


def _record_dirs():
    for shard_dir in sorted(ENTITIES_ROOT.iterdir()):
        if not shard_dir.is_dir():
            continue
        for record_dir in sorted(shard_dir.iterdir()):
            if record_dir.name.startswith("dea:metric-"):
                yield shard_dir, record_dir


def test_every_record_sits_at_its_id_derived_path():
    """No flat leftovers, no misplaced records: file location == record_relpath(id)."""
    misplaced = []
    for path in ENTITIES_ROOT.rglob("*.yaml"):
        if not path.parent.name.startswith("dea:metric-"):
            misplaced.append(f"{path}: not a record directory (stray yaml)")
            continue
        expected = BASE / record_relpath(path.parent.name)
        if path != expected:
            misplaced.append(f"{path}: expected {expected}")
    assert not misplaced, "records not at their id-derived paths:\n" + "\n".join(misplaced)


def test_every_record_directory_is_complete():
    incomplete = [
        f"{record_dir}: missing {name}"
        for _, record_dir in _record_dirs()
        for name in (f"{record_dir.name}.yaml", "README.md")
        if not (record_dir / name).is_file()
    ]
    assert not incomplete, "incomplete record directories:\n" + "\n".join(incomplete)


def test_shard_key_matches_directory():
    wrong = [
        f"{record_dir.name}: slug starts {record_dir.name.removeprefix('dea:metric-')[:1]!r} "
        f"but sits in {shard_dir.name!r}"
        for shard_dir, record_dir in _record_dirs()
        if shard_dir.name != shard_for_id(record_dir.name)
    ]
    assert not wrong, "records in the wrong shard:\n" + "\n".join(wrong)


def test_no_directory_approaches_the_github_listing_cap():
    root_entries = [p for p in ENTITIES_ROOT.iterdir()]
    assert len(root_entries) <= MAX_ROOT_ENTRIES, (
        f"entities/v1-alpha holds {len(root_entries)} entries "
        f"(cap {MAX_ROOT_ENTRIES}); the shard level is not holding"
    )
    oversized = []
    for shard_dir in sorted(ENTITIES_ROOT.iterdir()):
        if not shard_dir.is_dir():
            continue
        count = sum(1 for _ in shard_dir.iterdir())
        if count >= MAX_SHARD_ENTRIES:
            oversized.append(f"{shard_dir.name}/: {count} entries (trigger {MAX_SHARD_ENTRIES})")
    assert not oversized, "shards past the §4 trigger — subdivide (CR-MET-024 R4):\n" + "\n".join(oversized)


def test_catalog_paths_are_the_id_derived_paths():
    catalog = yaml.safe_load((BASE / "CATALOG.yaml").read_text())
    entities = (catalog or {}).get("catalog", {}).get("entities") or []
    stale = [
        f"{e['id']}: catalog says {e['path']}, layout says {record_relpath(e['id'])}"
        for e in entities
        if e.get("path") != record_relpath(e["id"])
    ]
    assert not stale, "CATALOG.yaml paths have drifted from the shard rule:\n" + "\n".join(stale)
