# dea:metric-ci-build-duration-95th-percentile

Candidate Performance Metric record for **CI Build Duration - 95th Percentile** (CIBD95) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ci-build-duration-95th-percentile`
- **Name:** CI Build Duration - 95th Percentile
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CIBD95

## 2. Definition

CI Build Duration - 95th Percentile (CIBD95) addresses how efficiently resources are converted into outputs and is a fixture of continuous integration reporting. It is computed as 95th Percentile Build Duration, expressed in minutes. It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
95th Percentile Build Duration
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2662 (batch 7)
