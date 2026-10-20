# Changelog

All notable changes to this catalog are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- CR-MET-009: catalog-establishment slice. 5-Metric pilot admitted:
  Customer Retention Rate, Mean Time to Recovery, Operating Margin,
  Data Completeness, Control Effectiveness Rate.
- 6 validation gates: `check_metric_schema.py`,
  `check_measurement_conformance.py`, `check_mece_coverage.py`,
  `check_evidence_anchors.py`, `check_threshold_semantics.py`,
  `check_dual_anchor.py`.
- 5 classification axes (CR-MET-002 binding).
- Dual-anchor requirement (CR-MET-009 §9 Q14).
- Schema mirror (`schemas/entity.schema.json`) of
  [dea-metamodel/schemas/entities/metric.json](https://github.com/technehub-labs/dea-metamodel).

### Changed
- `metamodel-pointer.yaml` migrated: `dea:entity-metric` -> `dea:PerformanceMetric`
  (CR-MET-001 re-membershiped canonical Metric).
- `legacy_ids` field added to metamodel-pointer to preserve historical references.

### Migration notes
- Existing contributors referencing `dea:entity-metric` should update to
  `dea:PerformanceMetric`. The `legacy_ids` array on the metamodel-pointer
  preserves backward compatibility for the allocation validator.