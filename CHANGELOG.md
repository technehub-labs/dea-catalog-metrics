# Changelog

All notable changes to this catalog are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- CR-MET-019: the admission readiness assessment. `scripts/admission_readiness.py`
  scores every candidate against exactly what the gates enforce for an
  admitted record, importing the dual anchor's constant sets rather than
  copying them, and writes the per-signature working set to
  `classifications/admission-readiness.yaml`; CI regenerates and diffs it.
  No candidate is admission-ready: all 4423 need the four admission-time
  fields, measurement evidence, and a bound formula, which is authoring work
  rather than derivation. The structural constraint is MECE: the corpus holds
  500 distinct signatures, 5 already admitted, so 495 have room for one more
  record, of which 120 are singletons and 375 are contested (largest cluster
  100 candidates). Enriching records does not change that number; only the
  axis model can. No record changes in this slice.
- CR-MET-017: canonical unit references at ingestion (Q19 ruling). The
  seed-value map gains a `unit_ref` section resolving the seed's 13 flat and
  plural spellings to the canonical form (`dea:unit-percent` to
  `dea:unit-ratio-percent`, `dea:unit-minutes` to `dea:unit-minute`, and the
  same singularisation for 11 more). Unit ids resolve by exact match, not by
  the hyphen normalisation the classification axes use. The 4423 candidate
  records are refreshed and bump to version 1.0.1 with a change-history
  entry; the 5 admitted records are unchanged. No record carries a flat or
  plural unit reference after the refresh.
- CR-MET-018: the domain and sector reconciliation input for the Q16
  enrichment slice. `scripts/reconcile_domain_sector.py` generates
  `classifications/domain-reconciliation.yaml` (286 seeded domain values)
  and `classifications/sector-reconciliation.yaml` (77 seeded sector
  values) from the corpus, and CI checks that the committed artefacts match
  it. Two findings, both derived from the data: the `domain` axis mixes
  functional areas with sector-scoped variants of them, and the corpus
  itself separates them (203 function values over 3338 records, 83
  sector-variant values over 1085 records, 0 mixed); and every seeded
  `sector` value names an INDUSTRY, so none maps to the metamodel's
  organisation-type vocabulary (`OrganizationalUnit.ou_type` holds
  structural forms, not industries). The ECF compound-domain mapping is
  deliberately left unresolved: it needs the domain-grounding discipline
  dea-metaframework owns. Nothing is renamed and no vocabulary is frozen.
- CR-MET-016: seed ingestion and the 4428-record corpus. The
  candidate-metrics seed workbook is committed at
  `seeds/open-deam-candidate-metrics-seed.xlsx` (sha-256
  `f037b8d3dfeb48538715e975492f4a864f56bfd58d66bed99afcad222a7af1c4`),
  and `scripts/ingest_seed.py` maps its fields and values onto the catalog
  schema through `classifications/field-aliases.yaml` and
  `classifications/seed-value-maps.yaml`. 4423 candidate records were
  ingested; 5 seed rows collide with the admitted pilot and are reported
  rather than written. A seed value with no mapping stops the ingestion.
- CR-MET-016: `scripts/report_coverage.py` reports how the corpus is
  distributed across the classification axes, the domains and the sectors. A
  report, not a gate.
- CR-MET-016: `scripts/_catalog.py`, a shared corpus loader using libyaml when
  the interpreter has it. Measured on this host, the schema gate went from
  23.8s to 2.8s, the measurement-conformance gate from 22.7s to 1.5s, and the
  MECE gate from 11.8s to 1.5s. A full eight-gate run is about 25s at 4428
  records.
- CR-MET-016: CI installs `openpyxl`, checks the corpus against the seed
  workbook, and prints the coverage report.
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
- CR-MET-016: the schema's required set is lifecycle-aware. A `candidate`
  record must carry the 15 fields the source provides; any other lifecycle
  must carry those plus the 4 admission fields (`subject_concept`,
  `measurement_nature`, `orientation_classification`,
  `measurement_nature_detail`). The seed has no column for any of them, so
  requiring them of a candidate would have meant inventing them for 4423
  records.
- CR-MET-016: the id pattern allows a leading digit (2 seed ids begin with
  one) and the abbreviation pattern allows letters in either case, digits, and
  the characters `% * / : . -` (1362 seed short forms use them). Both patterns
  were derived from the data's own character set.
- CR-MET-016: the subject vocabulary gained `operations` and `risk`, and the
  purpose vocabulary gained 9 values. Collapsing them would have thrown away
  the classification signal across 4423 records. The schema's enums and the
  `classifications/` vocabulary files are now identical for all five axes;
  they were not (the schema's purpose enum carried `quality` and the
  vocabulary file did not).
- CR-MET-016: the seed's formulas declare their operands, read off the
  published expression by splitting on the arithmetic and comparison
  operators. Without this the formula namespace gate reported 4423 unbound
  expressions, which made the finding meaningless.
- CR-MET-016: the pilot-count assertion is replaced by a corpus check that
  reads the workbook and asserts the id set and each record's provenance row.
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

### Known gaps
- The MTTR unit disagreement between the seed and the catalog is unresolved:
  the seed measures Mean Time to Recovery in hours, the catalog in minutes.
  The admitted record wins and is unchanged. This is Q18 in CR-MET-016.

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