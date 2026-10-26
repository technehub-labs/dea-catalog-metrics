# dea:metric-ci-build-duration-median

Candidate Performance Metric record for **CI Build Duration - Median** (CIBDM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ci-build-duration-median`
- **Name:** CI Build Duration - Median
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CIBDM

## 2. Definition

CI Build Duration - Median (CIBDM) captures how efficiently resources are converted into outputs for organizations tracking continuous integration. Its calculation is Median Minutes per Pipeline Run, measured in minutes. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
CIBDM = Median Minutes per Pipeline Run
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2661 (batch 7)
