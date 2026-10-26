# dea:metric-application-perceived-network-score

Candidate Performance Metric record for **Application-Perceived Network Score** (APNS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-application-perceived-network-score`
- **Name:** Application-Perceived Network Score
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APNS

## 2. Definition

Application-Perceived Network Score (APNS) captures the quality of outputs and outcomes for organizations tracking network performance & capacity. It is computed as Composite of Latency, Loss, Jitter against App Thresholds, expressed in score (points). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Composite of Latency, Loss, Jitter against App Thresholds
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3355 (batch 7)
