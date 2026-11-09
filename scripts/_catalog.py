"""Shared catalog loading for the gate scripts (CR-MET-016).

The corpus grew from 5 records to 4428, and every gate used to re-parse every
record from scratch. That made a full gate run minutes long. This module
loads the corpus once per process and uses libyaml when it is available.

The loaders are cached, so a gate process and a test session that imports
several gates pay the parse cost once.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import yaml

try:  # libyaml is roughly five times faster than the pure-Python parser
    from yaml import CSafeLoader as SafeLoader
except ImportError:  # pragma: no cover - depends on the interpreter build
    from yaml import SafeLoader

BASE = Path(__file__).parent.parent
ENTITIES_DIR = BASE / "entities"
ENTITIES_ROOT = ENTITIES_DIR / "v1-alpha"
SCHEMA_PATH = BASE / "schemas" / "entity.schema.json"
ALIAS_FILE = BASE / "classifications" / "field-aliases.yaml"
VALUE_MAP_FILE = BASE / "classifications" / "seed-value-maps.yaml"


def shard_for_id(metric_id: str) -> str:
    """The CR-MET-024 shard directory for a metric id.

    The slug is the id with the `dea:metric-` prefix removed. Lowercase
    ASCII letters shard to a single-letter directory; every other
    character (digit-leading slugs) shards to the `0-9` bucket. This is
    the only layout rule: the record path must stay derivable from the
    id alone (entity-storage-layout.md §5).
    """
    slug = metric_id.removeprefix("dea:metric-")
    ch = slug[:1]
    return ch if ch.isalpha() and ch.isascii() and ch.islower() else "0-9"


def record_relpath(metric_id: str) -> str:
    """The id-derived repository-relative path of a record file."""
    return f"entities/v1-alpha/{shard_for_id(metric_id)}/{metric_id}/{metric_id}.yaml"


def iter_record_yaml_paths():
    """Every Metric record file in the sharded tree, sorted by path."""
    for path in sorted(ENTITIES_ROOT.rglob("*.yaml")):
        if path.parent.name.startswith("dea:metric-"):
            yield path


@lru_cache(maxsize=1)
def load_metrics() -> tuple:
    """Every Metric record in the catalog, as (directory name, record) pairs."""
    metrics = []
    for path in iter_record_yaml_paths():
        if path.parent.name.startswith("dea:metric-"):
            metrics.append((path.parent.name, yaml.load(path.read_text(), Loader=SafeLoader)))
    return tuple(metrics)


@lru_cache(maxsize=1)
def load_metric_paths() -> tuple:
    """Every Metric record with its file path, as (path, record) pairs."""
    out = []
    for path in iter_record_yaml_paths():
        if path.parent.name.startswith("dea:metric-"):
            out.append((path, yaml.load(path.read_text(), Loader=SafeLoader)))
    return tuple(out)


@lru_cache(maxsize=1)
def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text())


@lru_cache(maxsize=1)
def load_aliases() -> dict:
    """Alias name -> canonical name."""
    data = yaml.load(ALIAS_FILE.read_text(), Loader=SafeLoader) or {}
    return {a: (s or {}).get("canonical") for a, s in (data.get("aliases") or {}).items()}


@lru_cache(maxsize=1)
def load_value_maps() -> dict:
    return yaml.load(VALUE_MAP_FILE.read_text(), Loader=SafeLoader) or {}
