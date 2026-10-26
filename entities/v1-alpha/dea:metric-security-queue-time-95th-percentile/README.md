# dea:metric-security-queue-time-95th-percentile

Candidate Performance Metric record for **Security Queue Time - 95th Percentile** (SQT95) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-queue-time-95th-percentile`
- **Name:** Security Queue Time - 95th Percentile
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SQT95

## 2. Definition

Security Queue Time - 95th Percentile (SQT95) captures the quality of outputs and outcomes for organizations tracking airport operations (deep dive). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Minutes waited by 95th percentile passenger, expressed in minutes. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Aviation.

## Formula

```
SQT95 = Minutes waited by 95th percentile passenger
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2272 (batch 6)
