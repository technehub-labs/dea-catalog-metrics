# dea:metric-cutover-runbook-compliance

Candidate Performance Metric record for **Cutover Runbook Compliance** (CRC-RM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cutover-runbook-compliance`
- **Name:** Cutover Runbook Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CRC-RM

## 2. Definition

Cutover Runbook Compliance (CRC-RM) measures conformance to standards, plans, or obligations in the Release Management & Environments domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Cutover Steps Executed per Runbook / Steps, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Cutover Steps Executed per Runbook / Steps
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** release_management_environments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2740 (batch 7)
