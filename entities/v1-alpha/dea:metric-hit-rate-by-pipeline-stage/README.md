# dea:metric-hit-rate-by-pipeline-stage

Candidate Performance Metric record for **Hit Rate by Pipeline Stage** (HRS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hit-rate-by-pipeline-stage`
- **Name:** Hit Rate by Pipeline Stage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** HRS

## 2. Definition

Hit Rate by Pipeline Stage (HRS) measures how effectively a process or entity achieves its intended outcome in the Sales domain. It is computed as Deals Advancing from Stage / Deals Entering Stage, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Deals Advancing from Stage / Deals Entering Stage
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 101 (batch 1)
