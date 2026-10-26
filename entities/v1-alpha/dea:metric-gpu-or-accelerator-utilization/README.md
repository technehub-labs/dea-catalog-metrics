# dea:metric-gpu-or-accelerator-utilization

Candidate Performance Metric record for **GPU or Accelerator Utilization** (GAU-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gpu-or-accelerator-utilization`
- **Name:** GPU or Accelerator Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GAU-M

## 2. Definition

GPU or Accelerator Utilization (GAU-M) measures the utilization or availability of capacity in the MLOps & Model Lifecycle Operations domain. It is defined as Used Accelerator Hours / Provisioned Hours; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Used Accelerator Hours / Provisioned Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2523 (batch 7)
