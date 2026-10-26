# dea:metric-post-merge-failure-rate

Candidate Performance Metric record for **Post-Merge Failure Rate** (PMFR-CI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-post-merge-failure-rate`
- **Name:** Post-Merge Failure Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PMFR-CI

## 2. Definition

Post-Merge Failure Rate (PMFR-CI) captures the quality of outputs and outcomes for organizations tracking continuous integration. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Failures on Main Branch / Runs on Main - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Failures on Main Branch / Runs on Main
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2672 (batch 7)
