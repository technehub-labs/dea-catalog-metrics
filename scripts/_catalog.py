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
SCHEMA_PATH = BASE / "schemas" / "entity.schema.json"
ALIAS_FILE = BASE / "classifications" / "field-aliases.yaml"
VALUE_MAP_FILE = BASE / "classifications" / "seed-value-maps.yaml"


@lru_cache(maxsize=1)
def load_metrics() -> tuple:
    """Every Metric record in the catalog, as (directory name, record) pairs."""
    metrics = []
    for path in sorted(ENTITIES_DIR.glob("v1-alpha/*/*.yaml")):
        if path.parent.name.startswith("dea:metric-"):
            metrics.append((path.parent.name, yaml.load(path.read_text(), Loader=SafeLoader)))
    return tuple(metrics)


@lru_cache(maxsize=1)
def load_metric_paths() -> tuple:
    """Every Metric record with its file path, as (path, record) pairs."""
    out = []
    for path in sorted(ENTITIES_DIR.glob("v1-alpha/*/*.yaml")):
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
