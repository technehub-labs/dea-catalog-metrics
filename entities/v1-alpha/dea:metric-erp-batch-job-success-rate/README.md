# dea:metric-erp-batch-job-success-rate

Candidate Performance Metric record for **ERP Batch Job Success Rate** (EBJS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-erp-batch-job-success-rate`
- **Name:** ERP Batch Job Success Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EBJS

## 2. Definition

ERP Batch Job Success Rate (EBJS) addresses the quality of outputs and outcomes and is a fixture of erp & enterprise application operations reporting. The formula is Successful Batch Runs / Scheduled Runs - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Successful Batch Runs / Scheduled Runs
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** erp_enterprise_application_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2168 (batch 6)
