# dea:metric-appraisal-contingency-fall-through-rate

Candidate Performance Metric record for **Appraisal Contingency Fall-Through Rate** (ACFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-appraisal-contingency-fall-through-rate`
- **Name:** Appraisal Contingency Fall-Through Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACFR

## 2. Definition

Appraisal Contingency Fall-Through Rate (ACFR) addresses exposure to adverse outcomes and is a fixture of real estate brokerage reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Contracts Falling through on Appraisal / Contracts, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Real estate practice.

## 3. Context

Measures deals collapsing at the appraisal contingency stage. It matters because appraisal gaps signal pricing exuberance and financing market stress. Fall-throughs can be hidden by re-coding collapsed deals as mutual withdrawals. Read with Sale-to-List Price Ratio and Days on Market to see whether appraisal failures are systematic market signal.

## Formula

```
ACFR = Contracts Falling through on Appraisal / Contracts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** real_estate_brokerage
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1017 (batch 3)
