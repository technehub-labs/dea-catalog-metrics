# CR-MET-018 -- Reconcile the Seeded Domain and Sector Vocabulary

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-26 |
| Depends on | CR-MET-016 (seed ingestion; seeded the domain and sector values); dea-metamodel CR-MET-005 (dimensionality vocabulary) |
| Blocks | the Q16 enrichment slice in dea-metaframework (board card #649) |
| Cardinal authority | dea-catalog-metrics (the corpus); dea-metamodel (the controlled entity names) |
| Kanban | board 9, card #649 |

## 1. Background and problem statement

CR-MET-016 ingested 4423 candidate records carrying 286 distinct `domain`
values and 77 distinct `sector` values as free text. CR-MET-015 left both
vocabularies open as Q16.

The owner ruled on Q16 (board card #642, 2026-10-26): the metamodel's
Business Function / Organization Function concept is the right home for
`domain`, and the organisation type is the right home for `sector`; the
current text stays as initial seeded data; the vocabulary is seeded from the
corpus but NOT frozen; and a follow-up slice enriches the related entities in
dea-metaframework so the seeded text can be reconciled into the metamodel's
controlled entity names.

This CR produces the reconciliation INPUT for that follow-up slice. It does
not perform the enrichment and it does not freeze anything.

## 2. What the corpus actually contains

Two findings, both derived from the data rather than assumed.

### F1: The `domain` axis mixes two things, and the corpus itself separates them

The seed's domain values name either a functional area (`finance_accounting`,
`human_resources`, `software_engineering`) or a sector-scoped variant of one
(`airport_operations`, `maritime_shipping`, `textile_apparel`). Read as a flat
list, the axis looks like a single vocabulary; it is not.

The corpus decides it per record: a record knows its own `sector`, and a
sector-scoped function names that industry inside its own name. Applying that
test across the corpus:

| Disposition | Seeded values | Records |
|---|---|---|
| function (names a functional area) | 203 | 3338 |
| sector_variant (names a sector-scoped area) | 83 | 1085 |
| mixed (both readings) | 0 | 0 |

Zero mixed values: the test is unambiguous on every seeded value. The 4423
seed-derived records carry one of the two dispositions.

58 of the seeded values are topic VARIANTS of a base function, marked by a
trailing `_deep_dive` (50 values) or `_standard_measures` (8 values).
Stripping the marker reduces 286 seeded values to 276 base functions; the
variant is the same functional area published as a focused measure set, not a
distinct function.

### F2: Every seeded `sector` value is an INDUSTRY, and the organisation-type
### vocabulary is a different axis

All 77 seeded sector values name an industry (`software`, `insurance`,
`manufacturing`, `financial_services`, `healthcare`, `media_entertainment`).
Not one names an organisational structure.

The metamodel's organisation-type vocabulary is
`OrganizationalUnit.ou_type`: `business-unit`, `division`, `department`,
`team`, `role-cluster`, `virtual-team`, `governance-body`,
`external-partner-role`. Those are structural forms of an organisation, not
industries. The ruling's premise ("the sector is a type of organization")
does not hold for the seeded data, and no seeded sector value maps to one.

The metamodel also has no industry entity: of its 283 entity ids, none names
an industry, sector, market or vertical. The closest controlled language for
"which area of the business" is the ECF compound-domain set that
dea-metaframework owns (7 values: `GovernanceAndExistence`,
`StrategyAndDirection`, `AgencyAndOrganization`, `PartyAndRelationship`,
`ProductAndValue`, `EnablementAndOperations`, `FinanceAndAccounting`).

## 3. Decisions (binding)

### D1: The seeded values are seed data, not vocabulary

The catalog keeps the seeded text as-is. Nothing is renamed, and no gate
freezes the value set. This is the ruling's "seed the vocabulary from the
corpus, but not freeze yet".

### D2: The reconciliation is a generated artefact, derived from the corpus

`scripts/reconcile_domain_sector.py` produces
`classifications/domain-reconciliation.yaml` and
`classifications/sector-reconciliation.yaml` from the corpus, and CI checks
that the committed artefacts match the corpus. A reconciliation that is
hand-maintained drifts from the corpus silently; a generated one cannot.

### D3: The ECF compound-domain mapping is left unresolved, deliberately

Each domain row carries `ecf_domain: null` with
`ecf_domain_status: unresolved`. That mapping requires the domain-grounding
discipline dea-metaframework owns: axiom grounding, semantic anchor, boundary
rules against adjacent domains, and the internal MECE partition. A keyword
rule cannot derive it, and a guessed mapping would be worse than an open
field, because it would look like a decision.

### D4: The Business Function records have no home yet

`dea:BusinessFunction` is admitted in the metamodel (L3, business profile,
`catalog_repo: null`). The 276 proposed function names therefore have no
repository to land in. The enrichment slice must decide where Business
Function records live; this CR names the gap and does not resolve it.

### D5: The sector axis keeps its industry meaning, and the org-type axis is
### separate

The seeded `sector` stays an industry. The organisation type, if the catalog
needs one, is a separate attribute governed by
`OrganizationalUnit.ou_type`. This CR records the axis distinction; whether
the catalog gains an `org_type` field is a decision for the enrichment slice
and for the owner.

## 4. Changes

1. `scripts/reconcile_domain_sector.py`: the generator.
2. `classifications/domain-reconciliation.yaml`: 286 rows, generated.
3. `classifications/sector-reconciliation.yaml`: 77 rows, generated.
4. `.github/workflows/validate-metrics.yml`: the drift check.
5. `CHANGELOG.md`.
6. `change-requests/CR-MET-018.md`, this document.

## 5. Decision points for the enrichment slice (board card #649)

### Q23: where do Business Function records live?

Open. `dea:BusinessFunction.catalog_repo` is null. The candidates are the
existing business-capabilities catalog, a new dedicated catalog, or
dea-metaframework alongside the domain grounding.

### Q24: does the catalog gain an organisation-type attribute?

Open. The seeded sector is an industry and the metamodel's org-type
vocabulary is a structural axis. The enrichment slice must say whether the
catalog carries `org_type` (from `ou_type`) alongside `sector` (industry).

### Q25: does the ECF compound-domain mapping land in dea-metaframework?

Open, and the follow-up slice's central question. The 276 base functions each
need a compound domain, with boundary rules where two functions sit on the
same boundary.

## 6. Definition of Done

- The generator runs and the committed artefacts match it (CI proves it).
- Every seeded domain value has exactly one disposition, and no value is
  mixed.
- Every seeded sector value carries the industry axis and states that no
  organisation-type value applies.
- The records themselves are untouched: the seeded text stays as seeded data.
- D-004, D-005, and the embargo denylist are clean on every touched file.

## 7. NOT-list

- No record changes; no value is renamed or removed.
- No vocabulary is frozen; no gate rejects a new domain or sector value.
- No ECF mapping is asserted.
- No Business Function record is created.
- No change to the metamodel.

## 8. References

- Board cards #642 (the Q16 ruling), #649 (the enrichment slice).
- CR-MET-015 (Q16 raised), CR-MET-016 (the values were seeded),
  CR-MET-017 (canonical unit references, sibling Q19 slice).
- dea-metamodel: `dea:BusinessFunction`, `OrganizationalUnit.ou_type`.
- dea-metaframework: `framework/domain-grounding.md`,
  `schemas/ecf-domain.schema.json`.
