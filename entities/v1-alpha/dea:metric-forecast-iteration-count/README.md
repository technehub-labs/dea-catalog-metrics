# dea:metric-forecast-iteration-count

Candidate Performance Metric record for **Forecast Iteration Count** (FIC-FP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-forecast-iteration-count`
- **Name:** Forecast Iteration Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FIC-FP

## 2. Definition

Forecast Iteration Count (FIC-FP) measures how efficiently resources are converted into outputs in the Financial Planning & Analysis domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Review Cycles needed per Forecast Sign-Off - reported in times per period. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Review Cycles needed per Forecast Sign-Off
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** financial_planning_analysis

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3793 (batch 8)
