# Changelog

All notable changes to this catalog are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- CR-MET-015: five field dimensions added to the catalog Metric schema.
  `abbreviation` and `unit` are required; `domain`, `sector`, and
  `source_credit` are optional. `abbreviation` must equal the left-hand
  variable of `formula_definition.expression`, so the short form is stated in
  one place. `unit` is coherent with `unit_ref` under the mechanical rule
  `unit_ref` is `dea:unit-<unit>` or `dea:unit-ratio-<unit>`. `source_credit`
  must appear among the record's `quality.measurement_evidence` entries.
  The pilot records are bumped 1.0.1 to 1.2.0.
- CR-MET-015: field-alias registry `classifications/field-aliases.yaml`, so a
  Metric authored against an external vocabulary can be ingested. The catalog
  keeps its canonical names; `subject_classification` is not renamed to
  `subject_area`, the two are synonyms at ingestion. Nine aliases are
  registered: `metric id`, `formula`, `unit id`, `subject_area`, `scope`,
  `purpose`, `orientation`, `significance`, `status`.
- CR-MET-015: `scripts/normalize_record.py`, the ingestion step that rewrites
  alias names to canonical ones, refuses a record carrying both spellings of
  one field with different values, and is idempotent on a canonical record.
- CR-MET-015: `scripts/check_field_alignment.py`, wired into CI as Gate 8. It
  checks that every alias resolves to a declared schema property, that no
  alias collides with a canonical name, that no stored record uses an alias
  name or carries both spellings, and the three field-coherence rules above.
- CR-MET-014: `description` is now a first-class required field of
  `schemas/entity.schema.json` (`{type: string, minLength: 1, maxLength: 2000}`,
  mirroring the normative `dea-metamodel/schemas/entities/metric.json`). All 5
  records carry it, populated from their README Definition prose, and are
  bumped to version 1.0.1 with a change-history entry. The field is projected
  into `CATALOG.yaml` by the regenerator. Before this CR a contributor writing
  `description` produced a silently accepted, inert field.
- Conformance tests: the record README `Definition` section must match the
  YAML `description` verbatim (whitespace-normalised), and
  `regenerate_catalog.py` must be idempotent across consecutive runs.
- CI: a registry-freshness step (`git diff --exit-code CATALOG.yaml`) fails a
  PR whose records were edited without regenerating.
- CR-MET-009: catalog-establishment slice. 5 Metric records admitted, all at
  version 1.0.0: Customer Retention Rate, Mean Time to Recovery, Operating
  Margin, Data Completeness, Control Effectiveness Rate. This is the pilot
  cohort, not a complete set.
- 7 numbered validation gates, wired into CI, plus a pytest run:
  `check_metric_schema.py`, `check_measurement_conformance.py`,
  `check_mece_coverage.py`, `check_evidence_anchors.py`,
  `check_threshold_semantics.py`, `check_dual_anchor.py`,
  `check_formula_namespace.py`. Gate 7 was added to the workflow in the
  documentation-realign slice; before that it existed and worked but no CI
  invoked it.
- 5 classification axes plus directionality (CR-MET-002 binding).
- Dual-anchor requirement (CR-MET-009 Section 9).
- Schema superset (`schemas/entity.schema.json`) over
  [dea-metamodel/schemas/entities/metric.json](https://github.com/technehub-labs/dea-metamodel).
  The catalog requires every field the normative schema requires, plus the
  classification axes and dual anchors that the normative entity does not carry.
  Containment, not equality, is the intended relationship.
- `test_schema_supersets_dea_metamodel_metric_json` reads the upstream schema
  and asserts containment, so an upstream schema change fails this catalog's CI.
  The previous revision checked a hardcoded field list and never opened the
  upstream file, so upstream drift could not fail it.

### Changed
- `metamodel-pointer.yaml` migrated: `dea:entity-metric` -> `dea:PerformanceMetric`
  (CR-MET-001 re-membershiped canonical Metric).
- `legacy_ids` field added to metamodel-pointer to preserve historical references.
- Repository positioning realigned to the metamodel. The GitHub description and
  topics previously described assessment and maturity content; this catalog
  publishes Performance Metric records bound to `dea:PerformanceMetric` and
  nothing else. `dea:Assessment` is a metamodel entity with no catalog binding
  and no catalog repository, so assessment semantics are out of scope here.
- README and CONTRIBUTING now state the metamodel binding, the
  `measurement-dimension` placement, and the rule that the catalog must not
  redefine the normative entity.

### Fixed
- CR-MET-014: `scripts/regenerate_catalog.py` no longer stamps the run date
  into `last_modified`; it derives the value from the record's own provenance
  (latest `metadata.change_history` date, falling back to `established_at`).
  Two consecutive runs on an unchanged tree now produce byte-identical output.
- CR-MET-014: removed the undeclared duplicate `status` field from
  `dea:metric-customer-retention-rate` (it duplicated `lifecycle_status` and
  was silently accepted by every gate).
- README layout block listed `contexts/v1-alpha/` and `validation/conformance/`,
  neither of which exists in this repository.
- Documentation claimed "6 validation gates" where CI runs 6 numbered gates
  plus pytest, and did not disclose that a 7th gate script
  (`check_formula_namespace.py`) existed but was not wired into CI. The gate is
  now wired, and both documents say so.
- CONTRIBUTING required "19 documentation sections" per record README. No record
  has 19 (actual counts 6, 6, 7, 11, 18), the count was never defined in
  FOUNDATIONS.md, and no gate enforced it. Replaced with a named section
  structure.
- CONTRIBUTING omitted two CI-enforced constraints that a new contributor hits
  immediately: the MECE 5-axis uniqueness collision, and
  `test_pilot_has_5_metrics`, which turns red on any record added until the
  same PR updates the count.

### Migration notes
- Existing contributors referencing `dea:entity-metric` should update to
  `dea:PerformanceMetric`. The `legacy_ids` array on the metamodel-pointer
  preserves historical references for tooling that resolves aliases.
- The `legacy_ids` array does NOT make the allocation validator tolerant of
  the old id. `validate_consumer.py` matches `entity_id` exactly and consults
  no alias map, so a pointer declaring `dea:PerformanceMetric` fails against
  every published OpenDEAM model tag, all of which carry `dea:entity-metric`.
  An earlier revision of this file claimed the opposite. Resolving that
  divergence is upstream work in `dea-architecture-framework`.