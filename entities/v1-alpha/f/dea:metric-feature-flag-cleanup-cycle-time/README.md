# dea:metric-feature-flag-cleanup-cycle-time

Candidate Performance Metric record for **Feature Flag Cleanup Cycle Time** (FFCCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-feature-flag-cleanup-cycle-time`
- **Name:** Feature Flag Cleanup Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FFCCT

## 2. Definition

Feature Flag Cleanup Cycle Time (FFCCT) captures the quality of outputs and outcomes for organizations tracking continuous delivery & deployment. It provides the day-to-day signal that a process is running as designed. Its calculation is Days from Flag Full Rollout to Removal, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
FFCCT = Days from Flag Full Rollout to Removal
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_delivery_deployment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2690 (batch 7)
