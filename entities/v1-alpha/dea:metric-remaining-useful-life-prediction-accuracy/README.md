# dea:metric-remaining-useful-life-prediction-accuracy

Candidate Performance Metric record for **Remaining Useful Life Prediction Accuracy** (RULPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-remaining-useful-life-prediction-accuracy`
- **Name:** Remaining Useful Life Prediction Accuracy
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RULPA

## 2. Definition

A Reliability & Maintainability Engineering (Deep Dive) indicator, Remaining Useful Life Prediction Accuracy (RULPA) quantifies the quality of outputs and outcomes. It is computed as Predicted RUL within Tolerance of Actual / Predictions, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how closely predicted asset life matches realized failure or replacement. Prediction accuracy is what makes RUL-based planning safe. Accuracy on assets that never reached failure is untested. Read with predictive maintenance coverage and asset health index (Deep Dive).

## Formula

```
Predicted RUL within Tolerance of Actual / Predictions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4107 (batch 9)
