# dea:metric-feature-store-coverage-ratio

Candidate Performance Metric record for **Feature Store Coverage Ratio** (FSCR-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-feature-store-coverage-ratio`
- **Name:** Feature Store Coverage Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FSCR-M

## 2. Definition

A MLOps & Model Lifecycle Operations indicator, Feature Store Coverage Ratio (FSCR-M) quantifies how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Features Served from Feature Store / Total Features Used; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of model features served from a governed feature store versus ad hoc pipelines. The feature store is the reuse-and-consistency layer of ML at scale: duplicated feature engineering wastes effort, and divergent online and offline computations create training-serving skew - one of the most insidious failure classes in production ML. Coverage must include consistent point-in-time correctness to be meaningful. Read with training-to-serving skew incidents (Deep Dive) and feature reuse rates.

## Formula

```
Features Served from Feature Store / Total Features Used
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2515 (batch 7)
