# Contributing to the Performance Metrics Catalog

This catalog accepts Metric records for the OpenDEAM metamodel. Each record
binds to the normative entity `dea:PerformanceMetric` (defined in
[dea-metamodel](https://github.com/technehub-labs/dea-metamodel),
`measurement-dimension`, class alias `MTR`, allocation `v0.2.1`).

A record publishes a *use* of that entity. It does not redefine it. See the
README for the full statement of scope and boundaries. The canonical scope,
classification model, dual-anchor model, MECE coverage target, and pilot
composition are in [docs/FOUNDATIONS.md](./docs/FOUNDATIONS.md).

## Quick start

1. Create `entities/v1-alpha/dea:metric-<slug>/`.
2. Add `dea:metric-<slug>.yaml` satisfying
   [schemas/entity.schema.json](./schemas/entity.schema.json). Since CR-MET-014
   this includes a required `description` field: the canonical human-readable
   definition of the record, mirroring the normative `metric.json` field of the
   same name.
3. Add a record `README.md` following the structure below. Its `Definition`
   section must match the YAML `description` verbatim; a conformance test
   compares them and fails if they diverge.
4. Regenerate the registry: `python3 scripts/regenerate_catalog.py`, and commit
   the resulting `CATALOG.yaml` in the same PR. Since CR-MET-014 the generator
   is idempotent and CI fails a PR whose registry is stale.
5. Open a PR. CI runs the gates.

Steps 4 and 5 are easy to miss, and step 5 alone will not fail CI in the way
you might expect. See the two constraints below.

## Constraints CI enforces that review will not catch

These were found by executing the quick start against a real clone, not by
reading it.

### 1. MECE uniqueness (gate 3)

The 5 classification axes plus directionality jointly define a Metric's
identity. Two records may not share the same signature, so copying an existing
record and renaming it fails:

```text
MECE conflict: ['dea:metric-data-completeness', 'dea:metric-<your-slug>'] share
(('information_architecture',), ('quality', 'compliance'), 'diagnostic',
 ('enterprise', 'business_domain'), 'higher_is_better')
```

Check your signature against the existing records before writing the record.
`python3 scripts/check_mece_coverage.py` is the arbiter, not a reviewer.

### 2. The corpus check (tests)

`tests/test_conformance.py` used to assert that the catalog holds exactly 5
records, the CR-MET-009 pilot cohort, frozen into a literal when the catalog
held nothing else. **Adding any record turned this test red until the same PR
updated the literal.** It was a pilot-era artifact.

It is replaced (CR-MET-016) by a check that reads the seed workbook and
asserts that every seed-derived record exists, that the set of ids matches the
workbook's, and that each record's provenance points back at its own workbook
row. A hard-coded count is replaced by a derived relationship, so adding a
record no longer requires editing a constant.

### 3. The lifecycle-aware required set (schema)

`schemas/entity.schema.json` splits its required fields by lifecycle. A
`candidate` record must carry the 15 fields the source provides:

`id`, `name`, `type`, `description`, `abbreviation`, `unit`, `version`,
`lifecycle_status`, `subject_classification`, `purpose_classification`,
`scope_classification`, `directionality`, `management_significance`.

Any other lifecycle must carry those plus the 4 admission fields:
`subject_concept`, `measurement_nature`, `orientation_classification`, and
`measurement_nature_detail`. Those four are requirements of ADMISSION, and
the seed workbook has no column for any of them.

### 4. Ingesting a seed workbook

The seed is a committed artefact, so ingestion is reproducible:

```bash
python3 scripts/ingest_seed.py --report   # what would be written, and any gap
python3 scripts/ingest_seed.py            # write the records
python3 scripts/ingest_seed.py --check    # does the corpus match the workbook?
```

Field NAMES come from `classifications/field-aliases.yaml`; field VALUES come
from `classifications/seed-value-maps.yaml`, which distinguishes `carry` (the
value is already a catalog value), `map` (it is a synonym) and `add` (it is a
distinct concept, so the catalog vocabulary gains it). A seed value that
appears in no map stops the ingestion:

```text
ingest_seed.py: no mapping for directionality value 'higher-is-better';
add it to seed-value-maps.yaml rather than guessing.
```

The ingestion owns the records it created: a seed-derived record is refreshed
on every run, so the corpus always matches the workbook. A record the catalog
admitted by another route is never overwritten; those ids are reported as
collisions.

## Record README structure

Earlier revisions of this file required "19 documentation sections". No record
in this catalog has 19, the count was never defined in
[docs/FOUNDATIONS.md](./docs/FOUNDATIONS.md), and no gate enforced it, so it was
unenforceable. The required structure is stated here instead, and it is what the
existing records should converge on:

| Section | Purpose |
|---|---|
| Identity | record id, name, version, lifecycle status |
| Definition | the canonical prose definition; must match the YAML `description` verbatim (CR-MET-014) |
| Formula | expression, inputs, output unit |
| Directionality | how the value is read |
| Classification | the 5 axes, with values |
| Dual anchors | measurable-entity kind, reputability tier |
| Measurement evidence | sources that support the definition |
| Interpretation | what a high or low value means |
| Metamodel anchor | `dea:PerformanceMetric`, dimension, class alias |
| Change history | CRs that established or revised the record |

Two existing records follow most of this structure
(`dea:metric-customer-retention-rate`, 18 sections;
`dea:metric-mean-time-to-recovery`, 11 sections). The other three have 6, 6, and
7 sections and are the ones to bring up to standard.

## Naming conventions

- Entity id: `dea:metric-<slug>` (lowercase, hyphen-separated).
- Formula id: `dea:formula-<slug>` (stable identifier when shared across Metrics).
- Unit id: `dea:unit-<name>` (per CR-MET-005 binding).

## Formula short forms

The left-hand variable in `formula_definition.expression` is the record's short
form. Two records may not bind a short form to semantically different
quantities, and a short form listed as reserved keeps one catalogue-wide
meaning. `MTTR` is reserved for Mean Time to Recovery; binding it to another
quantity is a blocking finding.

`scripts/check_formula_namespace.py` enforces this. **It is not yet wired into
CI**, so run it yourself before opening a PR:

```bash
python3 scripts/check_formula_namespace.py
```

## Lifecycle

| Status | Meaning |
|---|---|
| `candidate` | Pre-admission; dual anchors informational-only |
| `admitted` | Passed dual-anchor gate; published in CATALOG.yaml |
| `active` | In current use |
| `deprecated` | Should not be used in new models |
| `retired` | Historical record only |

## Validation gates

CI runs 13 steps: the regenerator, a registry-freshness check, a seed-corpus
check, a coverage report, 8 numbered gates, and pytest.

| Gate | Script |
|---|---|
| 1 | `check_metric_schema.py` |
| 2 | `check_measurement_conformance.py` |
| 3 | `check_mece_coverage.py` |
| 4 | `check_evidence_anchors.py` |
| 5 | `check_threshold_semantics.py` |
| 6 | `check_dual_anchor.py` |
| 7 | `check_formula_namespace.py` |
| 8 | `check_field_alignment.py` |

Gate 7 checks that a formula's short form does not rebind a reserved meaning.
Gate 8 checks the field-alias discipline and the coherence of the
CR-MET-015 field dimensions: `abbreviation` against the formula short form,
`unit` against `unit_ref`, and `source_credit` against the measurement
evidence.

## Field dimensions (CR-MET-015)

Two fields are required on every record:

| Field | Rule |
|---|---|
| `abbreviation` | The Metric's short form. It **must equal** the left-hand variable of `formula_definition.expression`, so there is one place the short form is stated. |
| `unit` | The plain unit label, e.g. `minute`, `percent`. Coherent with `unit_ref`: that must be `dea:unit-<unit>` or `dea:unit-ratio-<unit>`. |

Three more are optional:

| Field | Rule |
|---|---|
| `domain` | Business domain the Metric characterises. A free slug; no controlled vocabulary exists for Metric yet. |
| `sector` | Industry sector the Metric applies to. A free slug; no sector axis exists in the metamodel yet. |
| `source_credit` | Attribution for the Metric's definition. Must appear among the record's `quality.measurement_evidence` entries. |

## Ingesting a contribution written in another vocabulary

A Metric authored against an external field vocabulary may use an alias for
the catalog's canonical name, for example `subject_area` instead of
`subject_classification`, or `metric id` instead of `id`. The catalog does
**not** rename its own fields: the alias registry
[`classifications/field-aliases.yaml`](./classifications/field-aliases.yaml)
maps the external names onto the canonical ones, and the catalogue itself
stores only canonical names.

Canonicalise a contribution before you validate it:

```bash
python3 scripts/normalize_record.py <contribution.yaml> -o <canonical.yaml>
```

The normaliser rewrites alias names, refuses a record that carries both
spellings of one field with different values, and is idempotent on a record
that is already canonical.

## Versioning (CR-MM-04 R1)

- **Patch bump** on additive change (new optional field, new classification axis value).
- **Minor bump** on substantive change (reformulated formula, changed directionality).
- **Major bump** on breaking change (renamed Metric, removed field, changed identity).

## Provenance (CR-MM-04 R1)

- `metadata.established_by`: CR reference (e.g., `CR-MET-009`).
- `metadata.established_at`: ISO date.
- `metadata.change_history`: list of CRs with dates and change summaries.

## Dual anchors (CR-MET-009 Section 9)

- `measurable_entity_kind`: one of the 16 CR-MET-007 cross-domain subject types.
- `reputability_tier`: one of `industry_standard | framework_derived | sectoral_standard | internal_custom | emerging`.

Both are required for `admitted` records.