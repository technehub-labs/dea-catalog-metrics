# dea:metric-model-serving-latency-95th-percentile

Candidate Performance Metric record for **Model Serving Latency - 95th Percentile** (MSL95) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-serving-latency-95th-percentile`
- **Name:** Model Serving Latency - 95th Percentile
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MSL95

## 2. Definition

Model Serving Latency - 95th Percentile (MSL95) addresses the quality of outputs and outcomes and is a fixture of mlops & model lifecycle operations reporting. Its calculation is 95th Percentile Prediction Latency, measured in milliseconds (ms). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
95th Percentile Prediction Latency
```

## Unit

- **Unit reference:** `dea:unit-millisecond`
- **Unit:** millisecond
- **Unit label (as published):** milliseconds (ms)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2518 (batch 7)
