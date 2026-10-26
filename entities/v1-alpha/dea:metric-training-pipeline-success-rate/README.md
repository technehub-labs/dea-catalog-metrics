# dea:metric-training-pipeline-success-rate

Candidate Performance Metric record for **Training Pipeline Success Rate** (TPSR-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-training-pipeline-success-rate`
- **Name:** Training Pipeline Success Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TPSR-M

## 2. Definition

Training Pipeline Success Rate (TPSR-M) captures the quality of outputs and outcomes for organizations tracking mlops & model lifecycle operations. Its calculation is Training Runs Completing without Failure / Runs, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Training Runs Completing without Failure / Runs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2514 (batch 7)
