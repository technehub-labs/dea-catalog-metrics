# dea:metric-model-prediction-accuracy

Candidate Performance Metric record for **Model Prediction Accuracy** (MPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-prediction-accuracy`
- **Name:** Model Prediction Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MPA

## 2. Definition

Model Prediction Accuracy (MPA) measures the quality of outputs and outcomes in the Data Management & Analytics domain. The formula is Correct Model Predictions / Total Predictions - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how closely model outputs match observed outcomes on evaluation data. It matters because accuracy is the license for a model to influence decisions at all. It can be gamed via data leakage, cherry-picked test sets, or metrics mismatched to business cost. Read with Model Drift Index and out-of-sample validation results to confirm accuracy holds beyond the training regime.

## Formula

```
MPA = Correct Model Predictions / Total Predictions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 345 (batch 1)
