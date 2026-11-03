# CR-MET-022 -- Contribute the MAMA Automation-Measurement Candidate Records (3 Records)

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-11-04 |
| Depends on | CR-MET-009 (catalog establishment); CR-MET-014 (description field); CR-MET-015 (field dimensions); CR-MET-016 (seed-scale pipeline rules); CR-MET-020 (derived admission fields, subject_concept); CR-MET-021 (managed MAMA cross-reference relationship) |
| Blocks | none |
| Cardinal authority | dea-catalog-metrics (catalog); dea-metamodel (canonical semantics) |
| Kanban | board 9 |

## 1. Background and problem statement

CR-MET-021 established the managed cross-reference relationship with the MAMA
`mama-metrics` library and named three MAMA cards that have no adequate record
in this catalog: `automation-eligibility-share`, `worker-experience-impact`,
and `distributional-effects`. This CR contributes them through the normal
admission pipeline, adapting each card's construct to the catalog's
single-record-single-construct discipline.

The pipeline requirements observed: records satisfy
`schemas/entity.schema.json`; the record README `Definition` matches the YAML
`description` verbatim (whitespace-normalised); the classification axes use
the controlled vocabularies; the signature (including the CR-MET-020
`subject_concept` extension) is MECE-unique; `source_credit` appears among
`quality.measurement_evidence`; the registry and the subject-concept registry
are regenerated in the same change.

## 2. Objective

Add three MAMA-sourced candidate records with full provenance and bidirectional
references, extending the catalog's automation-measurement and governance
coverage without touching any existing record.

## 3. Proposed changes

| Record | Source card | Subject | Purpose | Scope | Direction | Significance | Dual anchor (kind / tier) |
|---|---|---|---|---|---|---|---|
| `dea:metric-automation-eligibility-share` | `automation-eligibility-share` (aligns_with) | business_architecture | capability | process | higher_is_better | operational, managerial | dea:BusinessProcess / framework_derived |
| `dea:metric-automation-oversight-burden` | `worker-experience-impact` (oversight-burden component; card broadens) | operations | risk | process | lower_is_better | operational, managerial | dea:BusinessProcess / framework_derived |
| `dea:metric-outcome-disparity-ratio` | `distributional-effects` (headline construct; card broadens) | governance | governance, risk | product_or_service | lower_is_better | managerial, regulatory | dea:Outcome / framework_derived |

### 3.1 Construct refinement (worker-experience-impact)

The MAMA `worker-experience-impact` card is deliberately a three-component
view (workload profile, oversight burden, validated survey) whose components
are reported separately and never summed. A single catalog record cannot
honestly carry a no-sum composite, so this CR admits the recordable core
component — oversight events per worker-day — as
`dea:metric-automation-oversight-burden`, with the external reference stating
the component relationship (`broadens`). The workload-profile and survey
components remain card-level guidance; they may become further records in a
later CR if admitted as single constructs.

### 3.2 Construct refinement (distributional-effects)

The MAMA `distributional-effects` card is a protocol (per-measure
between-group reporting, uncertainty-labelled gaps, suppression discipline).
The record condenses its headline construct into a single ratio
(`max_g Rate_g / min_h Rate_h`, 1.0 = parity) with the protocol's
preconditions carried as validation rules (documented groups, attribute
provenance, minimum cell volume). The card's fuller protocol remains the
method guidance referenced by the record.

### 3.3 Records

Each record: version 1.0.0, `lifecycle_status: candidate`,
`source_credit` = the MAMA library attribution (mirrored in
`quality.measurement_evidence`), one `external_references` item back to its
MAMA card (shape per CR-MET-021), `metadata.established_by: CR-MET-022`, and
a record README whose `Definition` matches the YAML `description`. No existing
record, classification, or schema file is modified.

### 3.4 Regenerated artefacts

- `scripts/regenerate_catalog.py` → `CATALOG.yaml` (3 new entries; counts
  4428 → 4431 candidates).
- `scripts/derive_subject_concepts.py` →
  `classifications/subject-concepts.yaml` (3 new concepts:
  `dea:subject-automation_eligibility_share`,
  `dea:subject-automation_oversight_burden`,
  `dea:subject-outcome_disparity_ratio`).

## 4. Non-goals

- No change to existing records, classifications, schemas, or gates.
- No lifecycle promotion: the records stay `candidate` until the dual-anchor
  admission assessment (per `classifications/admission-readiness.yaml` and
  the CR-MET-019 process) is run on them.
- No claim that MAMA endorses this catalog or vice versa; the CR-MET-021
  non-endorsement boundary stands.

## 5. Validation

- All gates run locally; the failing-gate set is identical to a pristine
  `main` checkout (pre-existing findings from the CR-MET-020 seed era; the
  schema, MECE, and evidence-anchor gates relevant to this change pass with
  0 findings including the new records).
- `python3 scripts/check_mece_coverage.py`: 0 MECE conflicts with the new
  signatures (each record's `subject_concept` is unique, per the CR-MET-020
  ruling).
- Registry and subject-concept registry regenerated in the same PR.

## 6. Risks and controls

| Risk | Control |
|---|---|
| Construct drift between card and record | `external_references` item on each record names the exact component relationship; MAMA-side mapping rows will be flipped to `mapped` in the MAMA repository after this CR lands |
| Composite-like reading of the oversight record | Record description and validation rules state the single-construct scope; the no-sum rule stays on the MAMA card |
| Disparity ratio misread as fairness proof | Known limitations state the parity-at-a-low-level and unchosen-axes failure modes; legal-interpretation boundary carried from the card |
| Premature lifecycle claims | All three records enter as `candidate`; admission is a separate assessed step |
