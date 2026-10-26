# dea:metric-dependency-lockfile-compliance

Candidate Performance Metric record for **Dependency Lockfile Compliance** (DLC-CI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dependency-lockfile-compliance`
- **Name:** Dependency Lockfile Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DLC-CI

## 2. Definition

Dependency Lockfile Compliance (DLC-CI) addresses conformance to standards, plans, or obligations and is a fixture of continuous integration reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Projects Using Locked Dependencies / Projects - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Projects Using Locked Dependencies / Projects
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
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2676 (batch 7)
