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

## Two constraints CI enforces that review will not catch

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

### 2. The pilot-count assertion (tests)

`tests/test_conformance.py` currently asserts:

```python
def test_pilot_has_5_metrics():
    assert n == 5, f"CR-MET-009: pilot must have 5 metrics (got {n})"
```

The number 5 is the CR-MET-009 pilot cohort, frozen into an assertion when the
catalog held exactly the pilot. **Adding any record turns this test red until
the same PR updates the literal.** This is a pilot-era artifact and is tracked
for removal; until then, update the count in the same PR and say why.

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

CI runs 7 checks: the regenerator, 6 numbered gates, and pytest.

| Gate | Script |
|---|---|
| 1 | `check_metric_schema.py` |
| 2 | `check_measurement_conformance.py` |
| 3 | `check_mece_coverage.py` |
| 4 | `check_evidence_anchors.py` |
| 5 | `check_threshold_semantics.py` |
| 6 | `check_dual_anchor.py` |
| (7) | `check_formula_namespace.py` **not wired; run it locally** |

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