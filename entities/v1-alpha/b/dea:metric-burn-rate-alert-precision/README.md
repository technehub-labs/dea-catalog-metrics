# dea:metric-burn-rate-alert-precision

Candidate Performance Metric record for **Burn Rate Alert Precision** (BRA-PREC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-burn-rate-alert-precision`
- **Name:** Burn Rate Alert Precision
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BRA-PREC

## 2. Definition

Burn Rate Alert Precision (BRA-PREC) captures the quality of outputs and outcomes for organizations tracking observability & site reliability engineering. The formula is Fast-Burn Alerts Corresponding to Real SLO Risk / Alerts - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
BRA-PREC = Fast-Burn Alerts Corresponding to Real SLO Risk / Alerts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2872 (batch 7)
