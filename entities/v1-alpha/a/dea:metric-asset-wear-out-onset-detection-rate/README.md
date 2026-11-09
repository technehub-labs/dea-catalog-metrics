# dea:metric-asset-wear-out-onset-detection-rate

Candidate Performance Metric record for **Asset Wear-Out Onset Detection Rate** (AWODR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-wear-out-onset-detection-rate`
- **Name:** Asset Wear-Out Onset Detection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AWODR

## 2. Definition

Asset Wear-Out Onset Detection Rate (AWODR) captures exposure to adverse outcomes for organizations tracking reliability & maintainability engineering (deep dive). It is defined as Wear-Out Phase Detected before Failure / Wear-Out Cases; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
AWODR = Wear-Out Phase Detected before Failure / Wear-Out Cases
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4108 (batch 9)
