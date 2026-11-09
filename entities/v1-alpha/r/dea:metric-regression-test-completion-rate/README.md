# dea:metric-regression-test-completion-rate

Candidate Performance Metric record for **Regression Test Completion Rate** (RTCR-QA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regression-test-completion-rate`
- **Name:** Regression Test Completion Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RTCR-QA

## 2. Definition

Regression Test Completion Rate (RTCR-QA) addresses conformance to standards, plans, or obligations and is a fixture of software testing & quality engineering reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Regression Runs Completed per Release / Required, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
RTCR-QA = Regression Runs Completed per Release / Required
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
- **Domain:** software_testing_quality_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2712 (batch 7)
