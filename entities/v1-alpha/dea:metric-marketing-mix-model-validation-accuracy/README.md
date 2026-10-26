# dea:metric-marketing-mix-model-validation-accuracy

Candidate Performance Metric record for **Marketing Mix Model Validation Accuracy** (MMMVA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-marketing-mix-model-validation-accuracy`
- **Name:** Marketing Mix Model Validation Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MMMVA

## 2. Definition

Marketing Mix Model Validation Accuracy (MMMVA) addresses the quality of outputs and outcomes and is a fixture of marketing & advertising standard measures (deep dive) reporting. The formula is Holdout Predicted vs Actual Revenue Variance - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how well MMM outputs predict outcomes on held-out or test data. Validation is the falsifiable test of marketing's most expensive model. Models validated on in-sample data grade their own homework. Read with attribution model coverage (Deep Dive) and incrementality testing coverage.

## Formula

```
Holdout Predicted vs Actual Revenue Variance
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing_advertising_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4348 (batch 11)
