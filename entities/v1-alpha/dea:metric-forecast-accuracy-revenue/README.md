# dea:metric-forecast-accuracy-revenue

Candidate Performance Metric record for **Forecast Accuracy (Revenue)** (FAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-forecast-accuracy-revenue`
- **Name:** Forecast Accuracy (Revenue)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FAR

## 2. Definition

Within Financial Planning & Analysis, Forecast Accuracy (Revenue) (FAR) is used to gauge the quality of outputs and outcomes. The formula is Absolute Variance of Forecast vs Actual / Actual - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how closely realized revenue tracks the forecast. Revenue forecast accuracy anchors guidance, hiring, and capacity decisions. Accuracy achieved through wide forecast bands is vagueness, not skill. Read with budget variance rate and revenue growth rate (Deep Dive).

## Formula

```
Absolute Variance of Forecast vs Actual / Actual
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3775 (batch 8)
