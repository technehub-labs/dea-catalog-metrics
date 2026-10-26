# dea:metric-code-churn-rate

Candidate Performance Metric record for **Code Churn Rate** (CCR-SD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-code-churn-rate`
- **Name:** Code Churn Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCR-SD

## 2. Definition

Within Software Development - Coding & Engineering Practices, Code Churn Rate (CCR-SD) is used to gauge the quality of outputs and outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Lines Rewritten shortly after Delivery / Lines Delivered - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Lines Rewritten shortly after Delivery / Lines Delivered
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_development_coding_engineering_practices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2654 (batch 7)
