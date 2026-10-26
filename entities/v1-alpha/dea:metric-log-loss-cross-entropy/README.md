# dea:metric-log-loss-cross-entropy

Candidate Performance Metric record for **Log Loss (Cross-Entropy)** (LOGL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-log-loss-cross-entropy`
- **Name:** Log Loss (Cross-Entropy)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LOGL

## 2. Definition

Log Loss (Cross-Entropy) (LOGL) captures the quality of outputs and outcomes for organizations tracking statistical model performance diagnostics. It is a working-level control: thresholds trigger immediate operational response. It is defined as Negative Log-Likelihood of Predicted Probabilities; the result is stated in score (points). It should be driven down, since lower readings signal healthier performance. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
Negative Log-Likelihood of Predicted Probabilities
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4063 (batch 9)
