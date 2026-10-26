# dea:metric-model-lift-top-decile

Candidate Performance Metric record for **Model Lift (Top Decile)** (LIFTD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-lift-top-decile`
- **Name:** Model Lift (Top Decile)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LIFTD

## 2. Definition

Model Lift (Top Decile) (LIFTD) captures the economic value created or preserved for organizations tracking statistical model performance diagnostics. It is a working-level control: thresholds trigger immediate operational response. It is defined as Response Rate in Top Decile / Overall Response Rate; the result is stated in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
Response Rate in Top Decile / Overall Response Rate
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4069 (batch 9)
