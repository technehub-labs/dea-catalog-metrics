# dea:metric-baseline-scope-stability

Candidate Performance Metric record for **Baseline Scope Stability** (BSS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-baseline-scope-stability`
- **Name:** Baseline Scope Stability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BSS

## 2. Definition

Baseline Scope Stability (BSS) addresses exposure to adverse outcomes and is a fixture of project management reporting. It is computed as 1 - Changed Scope / Baseline Scope, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how much the approved baseline scope has changed since approval. It matters because an unstable baseline makes every schedule and cost metric meaningless. Stability can look high because change requests sit unprocessed rather than rejected. Read with Requirements Change Rate and Milestone Adherence to distinguish genuine stability from a frozen change pipeline.

## Formula

```
1 - Changed Scope / Baseline Scope
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 363 (batch 1)
