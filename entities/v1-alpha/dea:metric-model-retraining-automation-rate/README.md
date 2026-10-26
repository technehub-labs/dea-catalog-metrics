# dea:metric-model-retraining-automation-rate

Candidate Performance Metric record for **Model Retraining Automation Rate** (MRAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-retraining-automation-rate`
- **Name:** Model Retraining Automation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MRAR

## 2. Definition

A MLOps & Model Lifecycle Operations indicator, Model Retraining Automation Rate (MRAR) quantifies capability maturity or development. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Automated Retraining Workflows / Retraining Workflows, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of retraining executed through automated, governed pipelines versus manual processes. Automation determines both response speed to drift and consistency of governance (every automated retraining can carry validation and approval gates built in), while manual retraining is slow, inconsistent, and audit-opaque. Automation of a bad process just makes it faster, so standardize the pipeline before automating it. Read with retraining trigger discipline and post-retraining performance validation.

## Formula

```
Automated Retraining Workflows / Retraining Workflows
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2528 (batch 7)
