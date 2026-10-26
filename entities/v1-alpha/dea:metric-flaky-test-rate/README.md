# dea:metric-flaky-test-rate

Candidate Performance Metric record for **Flaky Test Rate** (FTR-CI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-flaky-test-rate`
- **Name:** Flaky Test Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FTR-CI

## 2. Definition

Within Continuous Integration, Flaky Test Rate (FTR-CI) is used to gauge the quality of outputs and outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Tests Failing without Code Change / Test Runs - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Tests Failing without Code Change / Test Runs
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2667 (batch 7)
