# dea:metric-rollback-mean-time

Candidate Performance Metric record for **Rollback Mean Time** (RMT-CD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rollback-mean-time`
- **Name:** Rollback Mean Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RMT-CD

## 2. Definition

Rollback Mean Time (RMT-CD) measures how efficiently resources are converted into outputs in the Continuous Delivery & Deployment domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Minutes to Execute Rollback; the result is stated in minutes. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
RMT-CD = Minutes to Execute Rollback
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
- **Domain:** continuous_delivery_deployment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2702 (batch 7)
