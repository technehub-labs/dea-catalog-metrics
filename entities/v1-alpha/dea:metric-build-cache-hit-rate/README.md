# dea:metric-build-cache-hit-rate

Candidate Performance Metric record for **Build Cache Hit Rate** (BCHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-build-cache-hit-rate`
- **Name:** Build Cache Hit Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BCHR

## 2. Definition

A Continuous Integration indicator, Build Cache Hit Rate (BCHR) quantifies how efficiently resources are converted into outputs. Its calculation is Builds Using Cached Artifacts / Builds, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Builds Using Cached Artifacts / Builds
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2679 (batch 7)
