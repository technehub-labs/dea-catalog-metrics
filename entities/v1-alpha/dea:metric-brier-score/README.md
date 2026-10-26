# dea:metric-brier-score

Candidate Performance Metric record for **Brier Score** (BRIER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-brier-score`
- **Name:** Brier Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BRIER

## 2. Definition

A Statistical Model Performance Diagnostics indicator, Brier Score (BRIER) quantifies the quality of outputs and outcomes. It is a working-level control: thresholds trigger immediate operational response. It is defined as Mean Squared Error of Probabilistic Predictions; the result is stated in score (points). It should be driven down, since lower readings signal healthier performance. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
Mean Squared Error of Probabilistic Predictions
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4064 (batch 9)
