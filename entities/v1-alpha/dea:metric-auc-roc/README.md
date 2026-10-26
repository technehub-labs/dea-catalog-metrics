# dea:metric-auc-roc

Candidate Performance Metric record for **AUC-ROC** (AUCROC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-auc-roc`
- **Name:** AUC-ROC
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AUCROC

## 2. Definition

Within Statistical Model Performance Diagnostics, AUC-ROC (AUCROC) is used to gauge the quality of outputs and outcomes. It is defined as Area under Receiver Operating Characteristic Curve; the result is stated in score (points). In Software, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Area under Receiver Operating Characteristic Curve
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4059 (batch 9)
