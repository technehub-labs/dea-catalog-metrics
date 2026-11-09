# dea:metric-warranty-claims-prediction-variance

Candidate Performance Metric record for **Warranty Claims Prediction Variance** (WCPV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-warranty-claims-prediction-variance`
- **Name:** Warranty Claims Prediction Variance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WCPV

## 2. Definition

Warranty Claims Prediction Variance (WCPV) addresses the quality of outputs and outcomes and is a fixture of reliability & maintainability engineering (deep dive) reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Predicted vs Actual Claims Rate Variance, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
WCPV = Predicted vs Actual Claims Rate Variance
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4114 (batch 9)
