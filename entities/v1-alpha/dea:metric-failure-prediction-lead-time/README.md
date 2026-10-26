# dea:metric-failure-prediction-lead-time

Candidate Performance Metric record for **Failure Prediction Lead Time** (FPLT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-failure-prediction-lead-time`
- **Name:** Failure Prediction Lead Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FPLT

## 2. Definition

A Reliability & Maintainability Engineering (Deep Dive) indicator, Failure Prediction Lead Time (FPLT) quantifies the quality of outputs and outcomes. It is computed as Time between Predicted and Actual Failure, expressed in days. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how far in advance predicted failures are flagged before occurrence. Lead time is what converts prediction into planned, cheap intervention instead of outage. Lead times measured only on easy-to-predict failure modes overstate. Read with failure prediction accuracy and predictive maintenance coverage.

## Formula

```
Time between Predicted and Actual Failure
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4112 (batch 9)
