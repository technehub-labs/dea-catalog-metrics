# Contributing to the Performance Metrics Catalog

This catalog accepts Metric definitions for the OpenDEAM framework. Each Metric
must satisfy the requirements documented in [docs/FOUNDATIONS.md](./docs/FOUNDATIONS.md)
and pass all 6 validation gates.

## Quick start

1. Create a directory `entities/v1-alpha/dea:metric-<slug>/`.
2. Add `dea:metric-<slug>.yaml` with the full schema-compliant definition (see
   [schemas/entity.schema.json](./schemas/entity.schema.json)).
3. Add `README.md` covering the 19 documentation sections.
4. Open a PR. The 6 validation gates run on every push and PR.

## Naming conventions

- Entity id: `dea:metric-<slug>` (lowercase, hyphen-separated).
- Formula id: `dea:formula-<slug>` (stable identifier when shared across Metrics).
- Unit id: `dea:unit-<name>` (per CR-MET-005 binding).

## Lifecycle

| Status | Meaning |
|---|---|
| `candidate` | Pre-admission; dual anchors informational-only |
| `admitted` | Passed dual-anchor gate; published in CATALOG.yaml |
| `active` | In current use |
| `deprecated` | Should not be used in new models |
| `retired` | Historical record only |

## Versioning (CR-MM-04 R1)

- **Patch bump** on additive change (new optional field, new classification axis value).
- **Minor bump** on substantive change (reformulated formula, changed directionality).
- **Major bump** on breaking change (renamed Metric, removed field, changed identity).

## Provenance (CR-MM-04 R1)

- `metadata.established_by`: CR reference (e.g., `CR-MET-009`).
- `metadata.established_at`: ISO date.
- `metadata.change_history`: list of CRs with dates and change summaries.

## Dual anchors (CR-MET-009 §9)

- `measurable_entity_kind`: one of the 16 CR-MET-007 cross-domain subject types.
- `reputability_tier`: one of `industry_standard | framework_derived | sectoral_standard | internal_custom | emerging`.

Both required for `admitted` records.