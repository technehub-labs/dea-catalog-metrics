# dea:metric-pipeline-configuration-compliance

Candidate Performance Metric record for **Pipeline Configuration Compliance** (PCC-CI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pipeline-configuration-compliance`
- **Name:** Pipeline Configuration Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PCC-CI

## 2. Definition

Pipeline Configuration Compliance (PCC-CI) captures conformance to standards, plans, or obligations for organizations tracking continuous integration. The formula is Pipelines Using Approved Templates / Pipelines - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Pipelines Using Approved Templates / Pipelines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2671 (batch 7)
