# CR-MET-024 -- Shard the Entity Corpus by Slug First Letter; Rule the Seed/Enrichment Field Ownership

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-11-08 |
| Depends on | CR-MET-009 (catalog establishment); CR-MET-016 (seed-scale pipeline rules); CR-MET-018 (domain and sector reconciliation input, which rules the ECF mapping deliberately unresolved); CR-MET-021 (whose `external_references` enrichment ruling R6 preserves) |
| Blocks | future seed tranches (CR-MET-020 plan) are harder to review on a truncated directory; future cross-catalog consumers that resolve records by path |
| Cardinal authority | `dea-metaframework/docs/entity-storage-layout.md` (Ratified v1.0.0) §4 (shard rule) and §5 (path-integrity contract); dea-catalog-business-processes CR-BP-mv1 (post-nesting walker precedent) |
| Kanban | board 9 |

## 1. Background and problem statement

The corpus is 4,433 record directories flat under `entities/v1-alpha/`
(4,423 seed candidates per CR-MET-016, plus the 5 admitted pilot records
per CR-MET-009 and the 5 records contributed by CR-MET-022 and CR-MET-023).
GitHub truncates directory listings at 1,000 entries; the
`entities/v1-alpha` page currently reads:

> Sorry, we had to truncate this directory to 1,000 files. 3,433 entries
> were omitted from the list. Latest commit info may be omitted.

Two thirds of the corpus is therefore invisible to any browser-based
review, and the directory is guaranteed to grow: the CR-MET-020 tranche
plan contemplates the remaining seed tranches landing here.

The ratified org-wide storage contract anticipated exactly this failure
mode. `dea-metaframework/docs/entity-storage-layout.md` §1 requires the
layout to remain "permanently under the GitHub 1,000-entry directory
listing limit", §4 prescribes the remedy — "If any repo approaches 800
records, a shard level is introduced (e.g. by first letter of slug)
without changing the id system" — and §5 fixes the path-integrity
contract: "Every record's filesystem path must be derivable from its id."

This catalog is 4,433 records against an 800-record trigger, with no
shard level. The flat layout violates the ratified contract today.

While verifying the shard against this repository's own CI gates, a
second, independent defect surfaced: the seed-fidelity check
(`ingest_seed.py --check`) has been failing on `main` since the
CR-MET-021 landing (2026-11-04). CR-MET-021 attached
`external_references` (the managed MAMA cross-reference relationship)
and matching `metadata.change_history` entries to 11 seed-derived
records and re-serialized them with a different YAML dumper, while the
ingestion rebuilds each seed-derived record from the workbook and
demands byte-equality — a conflict that no storage-layout change can
repair and that blocks any PR in this repository from running green.
Because this CR's Definition of Done includes the repository's gate
suite, the seed/enrichment ownership ruling that resolves the conflict
is made here, in the same change.

## 2. The rulings

R1. **One shard level is introduced under `entities/v1-alpha/`, keyed on
the first character of the record slug.** The slug is the id with the
`dea:metric-` prefix removed. Lowercase ASCII letters shard to a
single-letter directory (`a/` … `z/`); every other character (today: the
two digit-leading slugs `3-d-secure-pass-rate` and
`30-day-readmission-rate-deep-dive`) shards to the `0-9/` bucket. The
resulting record path is
`entities/v1-alpha/<shard>/<dea:metric-...>/<dea:metric-...>.yaml`,
which is derivable from the id alone, satisfying §5.

R2. **The id system does not change.** Ids, record content, lifecycle
statuses, classification axes, READMEs and cross-references are
byte-identical before and after the migration. Only paths move.

R3. **Grouping by ECF coordinate or by classification value is
rejected.** The ECF compound-domain mapping is deliberately unresolved
in this catalog (CR-MET-018: every `ecf_domain` is `null`,
`ecf_domain_status` `unresolved`, pending domain grounding owned by
dea-metaframework), so there is no ECF key to shard on. The `domain`
field is a free-form, optional slug (~230 values, unset on the admitted
pilot records) and `subject_classification` is a multi-valued array;
sharding on either would key paths on mutable record content and break
the §5 id-derivability contract.

R4. **Bucket-size guard.** The measured distribution over the current
corpus has worst bucket `c/` = 603 entries; every bucket is below the
800-record trigger of §4. The new layout test asserts every shard stays
below 800 entries so the guard trips before GitHub does.

R5. **All tooling moves to the recursive walker in the same change.**
Every script, test and generated artefact that assumed the flat
two-level `v1-alpha/*/*.yaml` layout is updated in this CR; the
regenerated `CATALOG.yaml` carries the new `path:` values. This follows
the dea-catalog-business-processes precedent (CR-BP-mv1), where the
walker moved from a depth-limited glob to `rglob` when that catalog
nested its tree.

R6. **Fields the seed workbook has no column for are enrichment-owned.**
A seed-derived record the ingestion rebuilds must keep field content a
later CR attached to it. Concretely: `external_references` on the on-disk
record is merged back into the rebuilt record, re-inserted immediately
before `metadata` (the CR-MET-021 placement), and `metadata.change_history`
entries whose `cr` the seed does not emit are preserved verbatim and
appended. The merge is byte-stable across runs: merging the merged output
again changes nothing. Fields the workbook DOES own continue to be rebuilt
from the row; the collision guard still skips the 5 records admitted by
other routes, byte-untouched. The 11 enriched records were refreshed once
into the seed writer's canonical serialization (parsed content
byte-identical; folding/wrapping normalized), after which the seed check
passes and stays passing.

## 3. Proposed changes

### 3.1 Shared shard helpers (`scripts/_catalog.py`)

- `shard_for_id(metric_id)` — first slug character, else `0-9`.
- `record_relpath(metric_id)` — the id-derived repository-relative
  record path (the §5 contract, as code).
- `load_metrics()` / `load_metric_paths()` switch from
  `glob("v1-alpha/*/*.yaml")` to the recursive walk
  (`rglob("*.yaml")` under `entities/v1-alpha`, filtered to
  `dea:metric-*` parents), so all eight gates and the test suite follow
  automatically.

### 3.2 Writers and per-script loaders

- `scripts/regenerate_catalog.py` — recursive walk; each entry's `path`
  is emitted from `record_relpath(id)` (id-derived, not location-derived).
- `scripts/check_formula_namespace.py` — its private loader moves to the
  recursive walk.
- `scripts/ingest_seed.py` — `existing_ids()` moves to the recursive
  walk; the record writer creates
  `entities/v1-alpha/<shard>/<metric_id>/` so future seed tranches land
  pre-sharded; and per ruling R6, `merge_enrichment()` folds
  enrichment-owned field content (R6's `external_references` placement
  and non-seed `change_history` entries) back into every rebuilt
  seed-derived record, with `tests/test_seed_enrichment.py` pinning the
  merge semantics and running the whole-corpus check.
- `tests/test_conformance.py` — the two flat globs become recursive.

### 3.3 Migration and guard tooling

- `scripts/migrate_to_shard_layout.py` — idempotent migration: computes
  each record's target from its id, `git mv`s each record directory,
  and emits `reconciliation/migration-id-map.yaml` (id → previous path →
  new path) so downstream consumers can resolve stale paths. Re-running
  on a migrated tree no-ops. Each shard directory receives a short
  `README.md` naming the shard rule.
- `tests/test_layout.py` — the permanent guard: every `*.yaml` under
  `entities/v1-alpha` sits at exactly its `record_relpath()` location;
  every record directory carries `<id>.yaml` and `README.md`; every
  shard directory holds fewer than 800 entries; CATALOG.yaml paths equal
  the id-derived paths.

### 3.4 Regenerated artefacts

- `CATALOG.yaml` — all 4,433 `path:` values rewritten to the sharded
  form; `counts` unchanged (`total: 4433`, `admitted: 5`,
  `candidate: 4428`); every other entry field byte-identical (the
  regenerator is deterministic and derives `last_modified` from record
  provenance).
- `reconciliation/migration-id-map.yaml` — new, one entry per moved
  record.
- `README.md` repository-layout sketch — the `entities/v1-alpha/` line
  notes the shard level.
- `classifications/subject-concepts.yaml` and
  `classifications/admission-readiness.yaml` — regenerated against the
  current corpus (CI enforces byte-fidelity between these generated
  artefacts and the corpus). The regeneration surfaces drift that predates
  this CR: the two CR-MET-023 RAN subject concepts were never written into
  the committed vocabulary, and the readiness assessment is stale by the
  same interval. Landing the regenerated artefacts here repairs that drift;
  the record content that drives it is untouched.
- The 11 CR-MET-021-enriched seed-derived records (per ruling R6) —
  refreshed once into the seed writer's canonical serialization: parsed
  content byte-identical, YAML folding/wrapping normalized to the writer's
  form. No other record file changes.

## 4. Definition of Done

1. `find entities -name '*.yaml' | wc -l` reports 4,433 before and after
   the migration; no record file is created, deleted, or edited.
2. Every record directory satisfies
   `entities/v1-alpha/<shard>/<id>/` with `<id>.yaml` and `README.md`
   present, `<shard>` equal to `shard_for_id(<id>)` — asserted by
   `tests/test_layout.py`.
3. `entities/v1-alpha` itself holds at most 27 entries (26 letters +
   `0-9`), and every shard directory holds fewer than 800 entries.
4. `python3 scripts/regenerate_catalog.py` on the migrated tree is
   byte-idempotent (`git diff --exit-code CATALOG.yaml` clean), and
   `counts` are unchanged at 4433/5/4428.
5. `python3 scripts/ingest_seed.py --check` passes over the whole corpus —
   for the first time since 2026-11-04 (ruling R6). This proves both the
   writer's sharded path contract (a wrong path would report as a missing
   file, not a content match) and the enrichment merge: the 11
   CR-MET-021-enriched records keep their cross-references, every other
   seed record matches the workbook byte-for-byte, and the 5 records
   admitted by other routes are skipped untouched.
6. All eight gates exit 0 (`check_metric_schema`,
   `check_measurement_conformance`, `check_mece_coverage`,
   `check_evidence_anchors`, `check_threshold_semantics`,
   `check_dual_anchor`, `check_formula_namespace`, `check_field_alignment`).
7. `pytest tests/ -q` is green, including the new `test_layout.py`.
8. Every record id, every record README, and the parsed content of every
   record file are unchanged — except the 11 CR-MET-021-enriched seed
   records named in §3.4, whose parsed content is byte-identical and whose
   YAML serialization is normalized to the writer's canonical form:
   `git diff main --stat` shows only renames under `entities/`, those 11
   files, plus the tooling, CR, CHANGELOG, CATALOG, reconciliation and
   regenerated classification artefacts named in §3.

## 5. NOT-list

- No id changes, no lifecycle or classification changes, no record
  README changes. Record YAML files change only as named in §3.4: the
  11 CR-MET-021-enriched seed records' canonical re-serialization
  (parsed content byte-identical) — no other record content changes.
- No enrichment content is authored by the ingestion: `merge_enrichment`
  only preserves what a later CR wrote on disk; the seed workbook never
  gains `external_references` values from this CR.
- No claim of ECF domain resolution: the `domain`/`sector` fields and
  `domain-reconciliation.yaml` are untouched; ECF mapping remains with
  dea-metaframework (CR-MET-018 ruling stands).
- No schema change (`schemas/entity.schema.json` untouched); the shard
  is a storage-layout concern, not a record-semantics concern.
- No change to `00_inbox/` archived CR drafts.
- No governance-register or metaframework edits in this PR; the stale
  "root-position records" note in
  `dea-governance/registers/catalog-portfolio.yaml` and the flat-path
  assumption in the workspace `tools/emit_records.py` are named
  follow-ups for their own repos.
- No release cut; the CHANGELOG records the change under
  `[Unreleased]` per repo convention.

## 6. Risks and controls

| Risk | Control |
|---|---|
| A gate or test keeps a private flat glob and silently reads an empty set | §3 inventories every flat-layout site found by repo-wide grep for `v1-alpha`; DoD 6–7 prove each gate and the suite still sees all 4,433 records |
| Renames break git history readability | the migration uses `git mv` per record directory (rename detection applies), and `reconciliation/migration-id-map.yaml` maps every old path to its new one |
| A future admission lands flat and re-triggers the truncation | `ingest_seed.py` writes pre-sharded paths; `tests/test_layout.py` fails any misplaced record before CI merges it |
| A shard bucket grows past 800 as tranches land | R4's guard asserts < 800 per shard in CI; a future CR can subdivide a hot letter to 2-letter prefixes without touching ids |
| This PR's workflow run is misread as "broken by the reorg" when a red step is pre-existing | The seed-fidelity red is repaired in this CR (ruling R6) and `validate-metrics`' gates job is expected green on the PR. `validate-allocation` remains red on `main` independently (the v0.2.1 model pin predates the `dea:PerformanceMetric` rename), documented in the CHANGELOG Known gaps as a metamodel-versioning follow-up. Every step this CR touches is verified green locally (8 gates exit 0 seeing all 4,433 records; pytest 31/31; regen byte-idempotent; seed check PASS) |
| The enrichment merge silently drops or duplicates content | R6's merge is byte-stable (re-merging the output changes nothing), pinned by `tests/test_seed_enrichment.py`, and the whole-corpus check plus the 8 gates run on every push |

## 7. References

- `dea-metaframework/docs/entity-storage-layout.md` §1, §4, §5 (ratified v1.0.0)
- dea-catalog-business-processes: `scripts/_entity_walk.py`, `scripts/migrate_to_v3_layout.py` (CR-BP-mv1 precedent)
- GitHub directory truncation notice on `entities/v1-alpha` (1,000-entry cap)
- CR-MET-009, CR-MET-016, CR-MET-018, CR-MET-020 (corpus, pipeline, ECF deferral, tranche plan)
