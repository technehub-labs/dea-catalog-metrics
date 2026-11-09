#!/usr/bin/env python3
"""CR-MET-024: migrate the entity corpus to the slug-first-letter shard layout.

Moves every record directory from the flat
`entities/v1-alpha/<dea:metric-...>/` form to
`entities/v1-alpha/<shard>/<dea:metric-...>/`, where `<shard>` is the
first character of the slug (lowercase ASCII letters; everything else,
today the two digit-leading slugs, goes to `0-9`). Ids, record content
and record READMEs are untouched: this is a storage-layout move only.

The move is staged with `git mv` so rename detection preserves history,
and the script emits `reconciliation/migration-id-map.yaml` (id ->
previous path -> new path) so downstream consumers can resolve stale
paths. Each shard directory receives a short README naming the shard
rule.

Usage:
    python3 scripts/migrate_to_shard_layout.py --dry-run
    python3 scripts/migrate_to_shard_layout.py --execute
    python3 scripts/migrate_to_shard_layout.py --verify

The script is idempotent: re-running on a migrated tree no-ops.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import record_relpath, shard_for_id  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ENTITIES_ROOT = ROOT / "entities" / "v1-alpha"
MAP_PATH = ROOT / "reconciliation" / "migration-id-map.yaml"

GIT_MV_CHUNK = 50  # keep each git mv invocation well inside argv limits

SHARD_README = """# Shard `{shard}`

CR-MET-024 bucket for record slugs starting with `{shard}`. The shard
key is the first character of the id's slug (the id minus the
`dea:metric-` prefix); digit-leading slugs live in `0-9/`. The path
stays derivable from the id alone (entity-storage-layout.md §5):
`entities/v1-alpha/<shard>/<dea:metric-...>/<dea:metric-...>.yaml`.
"""


def flat_record_dirs() -> list[Path]:
    """Depth-1 `dea:metric-*` directories — the flat-era leftovers."""
    return sorted(
        p for p in ENTITIES_ROOT.iterdir()
        if p.is_dir() and p.name.startswith("dea:metric-")
    ) if ENTITIES_ROOT.exists() else []


def git_mv(sources: list[Path], dest_dir: Path) -> None:
    subprocess.run(
        ["git", "mv", *[str(s) for s in sources], str(dest_dir)],
        cwd=ROOT, check=True,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="plan the moves; write nothing")
    mode.add_argument("--execute", action="store_true", help="git mv the flat records into shards")
    mode.add_argument("--verify", action="store_true", help="assert the tree is fully migrated")
    args = ap.parse_args()

    if args.verify:
        stale = []
        for path in ENTITIES_ROOT.rglob("*.yaml"):
            if path.parent.name.startswith("dea:metric-") and path != ROOT / record_relpath(path.parent.name):
                stale.append(str(path))
        leftover = [str(p) for p in flat_record_dirs()]
        if stale or leftover:
            print("FAIL: tree is not fully migrated")
            for s in stale[:20]:
                print(f"  misplaced: {s}")
            for s in leftover[:20]:
                print(f"  flat:      {s}")
            return 1
        print("PASS: every record sits at its id-derived sharded path")
        return 0

    flat = flat_record_dirs()
    if not flat:
        print("PASS: nothing to migrate (no flat record directories at depth 1)")
        return 0

    planned: dict[str, list[tuple[Path, Path]]] = {}
    for record_dir in flat:
        shard = shard_for_id(record_dir.name)
        planned.setdefault(shard, []).append(
            (record_dir, ENTITIES_ROOT / shard / record_dir.name)
        )

    total = sum(len(moves) for moves in planned.values())
    print(f"flat record directories: {total}")
    for shard in sorted(planned):
        print(f"  {shard}/: {len(planned[shard])}")
    if args.dry_run:
        print("dry run: no changes written")
        return 0

    id_map = []
    for shard in sorted(planned):
        shard_dir = ENTITIES_ROOT / shard
        shard_dir.mkdir(parents=True, exist_ok=True)
        readme = shard_dir / "README.md"
        if not readme.exists():
            readme.write_text(SHARD_README.format(shard=shard))
        moves = planned[shard]
        for start in range(0, len(moves), GIT_MV_CHUNK):
            chunk = moves[start:start + GIT_MV_CHUNK]
            git_mv([src for src, _ in chunk], shard_dir)
        for src, dst in moves:
            id_map.append({
                "id": src.name,
                "from": str(src.relative_to(ROOT)),
                "to": str(dst.relative_to(ROOT)),
            })

    MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    MAP_PATH.write_text(yaml.dump(
        {
            "migration": "CR-MET-024",
            "rule": "entities/v1-alpha/<slug-first-letter|0-9>/<id>/<id>.yaml",
            "moved": len(id_map),
            "records": id_map,
        },
        sort_keys=False, width=100, allow_unicode=True,
    ))
    print(f"PASS: {len(id_map)} record directories moved; map written to {MAP_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
