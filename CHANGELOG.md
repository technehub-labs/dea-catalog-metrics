# Changelog

All notable changes to this catalog are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- CR-MET-009: catalog-establishment slice. 5 Metric records admitted, all at
  version 1.0.0: Customer Retention Rate, Mean Time to Recovery, Operating
  Margin, Data Completeness, Control Effectiveness Rate. This is the pilot
  cohort, not a complete set.
- 6 numbered validation gates, wired into CI, plus a pytest run:
  `check_metric_schema.py`, `check_measurement_conformance.py`,
  `check_mece_coverage.py`, `check_evidence_anchors.py`,
  `check_threshold_semantics.py`, `check_dual_anchor.py`.
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
- README layout block listed `contexts/v1-alpha/` and `validation/conformance/`,
  neither of which exists in this repository.
- Documentation claimed "6 validation gates" where CI runs 7 checks, and did not
  disclose that a 7th gate script (`check_formula_namespace.py`) exists and is
  unwired. That gate is proven by injection to catch a reserved-short-form
  violation that no wired gate sees.
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