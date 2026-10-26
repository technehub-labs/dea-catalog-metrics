# dea:metric-churn-model-recall

Candidate Performance Metric record for **Churn Model Recall** (CMR-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-churn-model-recall`
- **Name:** Churn Model Recall
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CMR-A

## 2. Definition

Within Customer Analytics & Insights, Churn Model Recall (CMR-A) is used to gauge the quality of outputs and outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as True Churners Identified / Actual Churners; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of actual churners the model correctly flags. Recall is the humane metric for churn: every missed churner is a lost-at-risk customer never offered a save. Recall and precision trade off, and business thresholds should reflect save-offer economics - cheap saves justify aggressive recall even at low precision. Always pair with the base churn rate, since recall on rare events can hide absolute misses. Read with propensity model lift and contract end churn risk conversion.

## Formula

```
True Churners Identified / Actual Churners
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** customer_analytics_insights

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1425 (batch 5)
