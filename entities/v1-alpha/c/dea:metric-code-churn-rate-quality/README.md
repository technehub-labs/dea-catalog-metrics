# dea:metric-code-churn-rate-quality

Candidate Performance Metric record for **Code Churn Rate (Quality)** (CHURNQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-code-churn-rate-quality`
- **Name:** Code Churn Rate (Quality)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CHURNQ

## 2. Definition

A Code Quality & Static Analysis indicator, Code Churn Rate (Quality) (CHURNQ) quantifies exposure to adverse outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Lines Rewritten within Window after First Write / Lines, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Software practice.

## Formula

```
CHURNQ = Lines Rewritten within Window after First Write / Lines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4178 (batch 9)
