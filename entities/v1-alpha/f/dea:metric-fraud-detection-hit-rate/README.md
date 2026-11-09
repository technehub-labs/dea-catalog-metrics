# dea:metric-fraud-detection-hit-rate

Candidate Performance Metric record for **Fraud Detection Hit Rate** (FDHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fraud-detection-hit-rate`
- **Name:** Fraud Detection Hit Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FDHR

## 2. Definition

Fraud Detection Hit Rate (FDHR) addresses exposure to adverse outcomes and is a fixture of insurance claims deep dive reporting. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Confirmed Fraud Cases / Cases Referred for Investigation; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Insurance, it is a recognized element of the standard performance toolkit.

## Formula

```
FDHR = Confirmed Fraud Cases / Cases Referred for Investigation
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1545 (batch 6)
