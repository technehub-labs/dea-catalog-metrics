# dea:metric-dead-code-ratio

Candidate Performance Metric record for **Dead Code Ratio** (DCR-CQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dead-code-ratio`
- **Name:** Dead Code Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DCR-CQ

## 2. Definition

Dead Code Ratio (DCR-CQ) measures the quality of outputs and outcomes in the Code Quality & Static Analysis domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Unreachable or Unused Code / Total Code; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
Unreachable or Unused Code / Total Code
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4187 (batch 9)
