# dea:metric-error-budget-burn-rate

Candidate Performance Metric record for **Error Budget Burn Rate** (EBBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-error-budget-burn-rate`
- **Name:** Error Budget Burn Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EBBR

## 2. Definition

Within SRE & Observability Standard Measures, Error Budget Burn Rate (EBBR) is used to gauge exposure to adverse outcomes. It is computed as Error Consumption Rate relative to Budget Allocation, expressed in ratio (x:1 or x). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
Error Consumption Rate relative to Budget Allocation
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4376 (batch 11)
