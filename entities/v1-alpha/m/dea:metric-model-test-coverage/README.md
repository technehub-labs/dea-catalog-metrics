# dea:metric-model-test-coverage

Candidate Performance Metric record for **Model Test Coverage** (MTC-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-test-coverage`
- **Name:** Model Test Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTC-M

## 2. Definition

Within MLOps & Model Lifecycle Operations, Model Test Coverage (MTC-M) is used to gauge the quality of outputs and outcomes. The formula is Models with Automated Test Suites / Models in Production - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
MTC-M = Models with Automated Test Suites / Models in Production
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2533 (batch 7)
