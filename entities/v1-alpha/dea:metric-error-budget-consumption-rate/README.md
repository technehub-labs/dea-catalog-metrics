# dea:metric-error-budget-consumption-rate

Candidate Performance Metric record for **Error Budget Consumption Rate** (EBCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-error-budget-consumption-rate`
- **Name:** Error Budget Consumption Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EBCR

## 2. Definition

Error Budget Consumption Rate (EBCR) addresses exposure to adverse outcomes and is a fixture of observability & site reliability engineering reporting. It is defined as Error Budget Consumed / Total Error Budget; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures how fast a service spends its allowed unreliability (100% minus SLO). The budget is the fair, data-driven arbiter between feature velocity and reliability work. Front-loaded spending early in a period is normal; sustained overspend is systemic. Read with error budget policy enforcement rate and service level objective attainment.

## Formula

```
Error Budget Consumed / Total Error Budget
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2861 (batch 7)
