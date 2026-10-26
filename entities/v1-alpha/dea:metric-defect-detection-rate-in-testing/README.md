# dea:metric-defect-detection-rate-in-testing

Candidate Performance Metric record for **Defect Detection Rate in Testing** (DDRT-QA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-defect-detection-rate-in-testing`
- **Name:** Defect Detection Rate in Testing
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DDRT-QA

## 2. Definition

Within Software Testing & Quality Engineering, Defect Detection Rate in Testing (DDRT-QA) is used to gauge the quality of outputs and outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Defects Found before Release / Total Defects - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the proportion of defects found in test stages versus those discovered post-release. Catching defects early is dramatically cheaper, and a healthy rate signals that test design mirrors real user behavior. A high rate can simply reflect weak production monitoring rather than excellent testing. Read with defect escape rate and incident caused by change rate.

## Formula

```
Defects Found before Release / Total Defects
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_testing_quality_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2708 (batch 7)
