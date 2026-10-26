# dea:metric-alert-to-case-conversion-rate

Candidate Performance Metric record for **Alert-to-Case Conversion Rate** (ACR-FC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alert-to-case-conversion-rate`
- **Name:** Alert-to-Case Conversion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ACR-FC

## 2. Definition

Alert-to-Case Conversion Rate (ACR-FC) addresses how efficiently resources are converted into outputs and is a fixture of insurance fraud & financial crime reporting. The formula is Cases Opened / Alerts Triaged - reported in percent (%). It is a standard measure in the Financial Services sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Cases Opened / Alerts Triaged
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_fraud_financial_crime
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2466 (batch 6)
