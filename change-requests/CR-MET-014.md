# CR-MET-014 -- Add a First-Class description Field to the Catalog Metric Schema

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-25 |
| Depends on | CR-MET-009 (catalog establishment) |
| Blocks | none |
| Cardinal authority | dea-catalog-metrics (catalog); dea-metamodel (canonical semantics) |
| Kanban | board 9 |

## 1. Background and problem statement

A Metric record in this catalog has no declared `description` field. Board
card #602 established that the prose describing a metric lives in four places
with four different names:

1. `dea-metamodel` entity YAML: `definition` (the entity's meaning; upstream by
   design).
2. `dea-metamodel/schemas/entities/metric.json`: `description`
   (`{type: string, maxLength: 2000}`, optional).
3. This catalog's `schemas/entity.schema.json`: neither; the prose carrier is
   `measurement_nature_detail` (required).
4. The record README: `## 2. Definition`.

Verified consequence: a contributor writing the natural `description` field
receives no error, no warning, and no gate failure. `schemas/entity.schema.json`
leaves `additionalProperties` unset, so the unknown property is silently
accepted, and `scripts/regenerate_catalog.py` does not project it, so it never
reaches `CATALOG.yaml`. The field is inert. This was proven by injection in a
throwaway clone: all seven gates exited 0 and pytest passed with the injected
field present.

A second verified defect exists in the same area: the README `## 2. Definition`
prose and the YAML `measurement_nature_detail` prose are not identical for any
of the five records, neither is derived from the other, and no gate compares
them. For three records the README is richer (it carries the measurement
boundary); for two it is shorter (it drops CR-binding notes the YAML carries).
Prose about the same metric therefore disagrees across surfaces.

## 2. Objective

Add `description` as a first-class, required, validated, and projected field of
the catalog Metric schema, aligned with the normative schema's field of the
same name, so that:

- a contributor writing `description` writes a real field, not an inert one;
- every record carries exactly one canonical human-readable definition;
- the record README `## 2. Definition` section is checked against it, closing
  the prose-divergence gap;
- the catalog registry projects it, so consumers see it without opening each
  record file.

## 3. Decisions (binding)

### D1: Field shape mirrors the normative schema

`description: {type: string, minLength: 1, maxLength: 2000}`. The normative
`dea-metamodel/schemas/entities/metric.json` declares
`{type: string, maxLength: 2000}`; the catalog adds `minLength: 1` because the
field is required here and an empty string must not satisfy it.

### D2: The field is required

The catalog schema already requires its other prose carrier
(`measurement_nature_detail`); a record without a human-readable definition is
not publishable in a catalog whose consumers are human readers. Required status
is enforced by Gate 1 (`check_metric_schema.py`) with no new gate. The catalog
schema remains a strict superset of the normative required set, which does not
include `description`; superset direction is unchanged.

### D3: Canonical content is the record README `## 2. Definition` prose

For all five pilot records the README Definition is the human-facing,
reviewed prose and (for three records) the richer text. It becomes the YAML
`description`. A new conformance test asserts the README Definition section
matches the YAML `description` verbatim (whitespace-normalised), so the two
surfaces can no longer diverge silently.

### D4: `measurement_nature_detail` is left unchanged in this CR

The schema documents it as the description of the measurement nature (example:
"ratio expressed as percentage"), while the pilot records use it for fuller
prose, including CR-binding notes on two records. Narrowing it would delete
provenance (`Demonstrates the binding WEIGHTED_MEAN aggregation rule...`) that
has no other declared home. The resulting overlap with `description` is
recorded as an open question (Q15) rather than resolved unilaterally.

### D5: The registry projects `description`

`scripts/regenerate_catalog.py` adds `description` to each per-entity entry in
`CATALOG.yaml`. A field that is validated but never surfaced is the same trap
in a second location.

### D6: `last_modified` becomes a record fact, not the run date (fixes the generator idempotence defect, board card #580)

The regenerator currently stamps `str(date.today())` into every entry, so
every run dirties the tracked registry and the file can never be drift-checked.
It now derives `last_modified` from the record's own latest
`metadata.change_history` date (falling back to `metadata.established_at`).
Both are real per-record provenance fields required by CR-MM-04 R1. Two
consecutive runs on an unchanged tree now produce byte-identical output, which
a new conformance test asserts. CI gains a registry-freshness step
(`git diff --exit-code CATALOG.yaml`) that the idempotent generator makes
possible; a contributor who edits a record without regenerating now fails CI.

### D7: The undeclared duplicate `status` field is removed from one record

`dea:metric-customer-retention-rate` carries `status: admitted`, an undeclared
duplicate of `lifecycle_status: admitted` that every gate silently accepts for
the same reason the `description` injection passed. It is removed. House style
across the organisation sets `additionalProperties` on zero of 139 metamodel
entity schemas, so this CR does not set it either; removing the live duplicate
is the pragmatic closure.

## 4. Changes

1. `schemas/entity.schema.json`: add `description` property and add it to
   `required`.
2. All five records under `entities/v1-alpha/`: add `description` (from the
   README Definition prose), bump `version` 1.0.0 -> 1.0.1 (patch: additive
   field, per the catalog versioning rule), and append a
   `metadata.change_history` entry referencing this CR.
3. `dea:metric-customer-retention-rate`: remove the undeclared `status` field.
4. `scripts/regenerate_catalog.py`: project `description`; derive
   `last_modified` from record provenance instead of the run date.
5. `tests/test_conformance.py`: new tests for README/YAML description
   consistency and generator idempotence; extend the schema-superset field list
   with `description`.
6. `.github/workflows/validate-metrics.yml`: add a registry-freshness step.
7. `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`: state where the description
   lives and that the registry is freshness-checked.

## 5. Decision points

### Q15: Should `measurement_nature_detail` be narrowed to its schema-stated purpose?

Open. With `description` present, the pilot content of
`measurement_nature_detail` substantially duplicates it. Narrowing to the
nature-expression note would delete two CR-binding provenance sentences that
have no other declared home, so this CR does not do it. Disposition is for the
owner: narrow (and relocate the provenance), or accept the overlap.

## 6. Definition of Done

- Gate 1 fails a record that omits `description` or sets it to an empty string
  (proven by mutation in a throwaway clone).
- The README/YAML consistency test fails when either surface is edited alone
  (proven by mutation).
- Two consecutive `regenerate_catalog.py` runs produce byte-identical
  `CATALOG.yaml` (asserted by a test).
- All eight gate scripts exit 0 and the full test suite passes.
- D-004, D-005, and the embargo denylist are clean on every touched file.

## 7. NOT-list

- No change to `dea-metamodel`; its `metric.json` already declares
  `description`.
- No `additionalProperties: false` (house style; see D7).
- No narrowing of `measurement_nature_detail` (Q15).
- No change to the upstream allocation drift (board card #600), which is
  unrelated and lives in dea-architecture-framework.

## 8. References

- Board cards #601 (the 16 required attributes; now 17), #602 (the four-places
  finding), #580 (generator idempotence).
- CR-MET-009 (catalog establishment).
- `dea-metamodel/schemas/entities/metric.json` (normative `description`).
