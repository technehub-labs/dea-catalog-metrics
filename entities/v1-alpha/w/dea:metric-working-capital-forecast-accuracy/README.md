# dea:metric-working-capital-forecast-accuracy

Candidate Performance Metric record for **Working Capital Forecast Accuracy** (WCFA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-working-capital-forecast-accuracy`
- **Name:** Working Capital Forecast Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WCFA

## 2. Definition

A Financial Planning & Analysis indicator, Working Capital Forecast Accuracy (WCFA) quantifies the quality of outputs and outcomes. The formula is Variance of Forecast vs Actual Working Capital / Actual - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how well projected working capital tracks actuals. Working capital surprises are financing surprises. Accuracy on averages while missing quarter-end swings misses the cash reality. Read with working capital productivity (Deep Dive) and cash conversion cycle (Working Capital).

## Formula

```
WCFA = Variance of Forecast vs Actual Working Capital / Actual
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** financial_planning_analysis

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3785 (batch 8)
