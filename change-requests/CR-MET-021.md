# CR-MET-021 -- Managed Cross-Reference Relationship with the MAMA Metric Library (mama-metrics)

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-11-04 |
| Depends on | CR-MET-009 (catalog establishment); CR-MET-014 (description field); CR-MET-015 (field dimensions) |
| Blocks | none |
| Cardinal authority | dea-catalog-metrics (catalog); dea-metamodel (canonical semantics) |
| Kanban | board 9 |

## 1. Background and problem statement

MAMA (Measuring Automation & Measuring Autonomy) is an open framework and
toolset organization ([Measuring-Automation-Managing-Autonomy](https://github.com/Measuring-Automation-Managing-Autonomy))
whose `mama-metrics` repository publishes a versioned library of
automation-measurement metric cards: definitions of what to measure about
automated work — coverage, performance, quality, exceptions/reliability,
cost/value, human/customer impact, distributional effects — with automation
denominators, adverse-effect pairing, attribution and uncertainty rules.

Both catalogs now define overlapping performance-metric semantics (this
catalog holds 4,428 records including automation-specific ones such as
`dea:metric-straight-through-processing-rate-automation`,
`dea:metric-automation-ratio`, and `dea:metric-escalation-rate-llm-to-human`;
`mama-metrics` holds 18 cards). Without a managed relationship, the two
corpora will drift: same words meaning different things, divergent
denominators, and no way to trace which definition a consumer used.

The catalog schema already carries an `external_references` field
(CR-MET-015 field dimensions), but its items are untyped and no record uses
it.

## 2. Objective

Establish a managed, version-pinned, bidirectionally documented
cross-reference relationship between this catalog and `mama-metrics`, such
that:

1. every cross-reference in either direction is recorded, typed, and carries a
   meaning note;
2. the referenced records' existence and lifecycle status are CI-checkable at
   a pinned commit;
3. meanings stay distinct — neither side redefines the other's constructs.

## 3. Proposed changes

### 3.1 `external_references` item shape (additive schema documentation)

CR-MET-021 defines the canonical item shape for `external_references` and
documents it in `schemas/entity.schema.json` (required: `source`,
`source_id`, `url`, `relationship`; optional: `note`, `recorded_by`;
`additionalProperties` remains true for other frameworks). The `relationship`
vocabulary is stated **from the referenced external item's perspective
relative to this record**: `aligns_with` (same construct and scope),
`narrows` (the external item is this construct restricted to a narrower
context), `broadens` (the external item covers a wider construct),
`complements`, `references`.

The field remains optional; no existing record changes meaning.

### 3.2 Back-references seeded on 12 records

Twelve records matched by the MAMA crosswalk gain one `external_references`
item each, pointing at the corresponding `mama-metrics` card, plus a
`metadata.change_history` entry:

| Record | MAMA card | Relationship |
|---|---|---|
| dea:metric-automation-potential-realized-rate | automation-coverage | aligns_with |
| dea:metric-straight-through-processing-rate-automation | straight-through-completion-rate | aligns_with |
| dea:metric-bot-success-rate | task-success-rate | broadens |
| dea:metric-first-pass-yield | output-quality-rate | aligns_with |
| dea:metric-application-response-time | service-latency | broadens |
| dea:metric-exception-handling-rate | exception-rate | aligns_with |
| dea:metric-escalation-rate-llm-to-human | escalation-rate | broadens |
| dea:metric-achieved-availability | availability | aligns_with |
| dea:metric-mean-time-to-recovery | recovery-time | narrows |
| dea:metric-customer-satisfaction-score | customer-impact | broadens |
| dea:metric-benefits-realization-ratio | realized-vs-forecast-benefit | narrows |
| dea:metric-human-in-the-loop-intervention-rate | human-touch-ratio | broadens |

No `description`, formula, classification, or lifecycle field is modified.
`lifecycle_status` is untouched (12 × candidate, 1 × admitted in the list
above is unchanged by this CR).

### 3.3 Relationship statement (README)

A "Related frameworks" section is added to the README documenting the
relationship, its single source of truth (the MAMA-side mapping file
`mama-metrics/external/dea-mapping.yaml`, pinned to this catalog's commit
`c2a2951a8a4f437817e293cd12593b4e70176f4d`), and the non-endorsement
boundary.

### 3.4 Proposed future candidates (not ingested by this CR)

The MAMA crosswalk marks three cards as having no adequate record in this
catalog and proposes them as future candidate records through the normal
admission pipeline (dual-anchor, MECE signature check):

- `automation-eligibility-share` (share of assessed work volume that is
  eligible for automation — the precondition construct behind
  Automation Ratio and Automation Potential Realized Rate);
- `worker-experience-impact` (workload profile + oversight burden + validated
  survey, baseline-before-change);
- `distributional-effects` (between-group outcome/failure distribution with
  small-cell suppression and attribute-provenance rules).

This CR does **not** ingest them; each will arrive as its own record-level CR
with source attribution to `mama-metrics`.

## 4. Non-goals

- No change to any record's definition, formula, classifications, or
  lifecycle status.
- No change to the normative `dea:PerformanceMetric` entity (that belongs to
  `dea-metamodel`).
- No bulk import of MAMA cards; the catalog's admission pipeline (MECE,
  dual-anchor, seed provenance) stays the only path to new records.
- No claim of equivalence, endorsement, or conformance in either direction.
  MAMA's autonomy method (lowercase `mama`,
  `emmanuel-a-otchere/MeasuringAndManagingAutonomy`) is unrelated to this
  crosswalk.

## 5. Validation

- `python3 scripts/regenerate_catalog.py` re-run; the resulting
  `CATALOG.yaml` (12 × `last_modified` bump) is committed in the same PR per
  the contributing rules.
- Full conformance suite (`pytest tests/`) passes locally.
- The MAMA-side validator
  (`mama-metrics/tools/validate_external_refs.py --catalog <clone>`) verifies
  record existence and lifecycle at the pinned commit; it runs in MAMA's CI
  against the commit this CR lands on.

## 6. Risks and controls

| Risk | Control |
|---|---|
| Divergent meanings after upstream edits | Mapping rows carry meaning notes; MAMA CI fails on lifecycle drift at the pinned commit and forces row review |
| Cross-references mistaken for equivalence | Non-endorsement boundary stated in both READMEs and in the MAMA-side policy |
| Schema tightening breaks other frameworks | `additionalProperties` stays true; the field remains optional |
| Reference rot (record retires/deprecates) | MAMA validator flags status mismatch; re-pin requires a MAMA-side review record |
