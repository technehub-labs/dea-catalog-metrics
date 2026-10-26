# dea:metric-shrinkage-rate-deep-dive

Candidate Performance Metric record for **Shrinkage Rate (Deep Dive)** (SHR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shrinkage-rate-deep-dive`
- **Name:** Shrinkage Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SHR-D

## 2. Definition

Shrinkage Rate (Deep Dive) (SHR-D) measures the utilization or availability of capacity in the Contact Center Operations (Deep Dive) domain. The formula is Non-Productive Time / Scheduled Time - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Non-Productive Time / Scheduled Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2478 (batch 6)
