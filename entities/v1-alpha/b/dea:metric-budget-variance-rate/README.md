# dea:metric-budget-variance-rate

Candidate Performance Metric record for **Budget Variance Rate** (BVR-FP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-budget-variance-rate`
- **Name:** Budget Variance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BVR-FP

## 2. Definition

Budget Variance Rate (BVR-FP) addresses the quality of outputs and outcomes and is a fixture of financial planning & analysis reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Absolute Variance vs Budget / Budget; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures deviation of actual results from the approved budget. Variance is the primary control signal of financial discipline. Variance tolerance defined too loosely makes the metric decorative. Read with cost variance - IT budget (Deep Dive) and budget forecast accuracy - financial planning (Deep Dive).

## Formula

```
BVR-FP = Absolute Variance vs Budget / Budget
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** financial_planning_analysis

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3776 (batch 8)
