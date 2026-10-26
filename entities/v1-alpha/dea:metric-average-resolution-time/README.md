# dea:metric-average-resolution-time

Candidate Performance Metric record for **Average Resolution Time** (ART) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-resolution-time`
- **Name:** Average Resolution Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ART

## 2. Definition

Within Customer, Average Resolution Time (ART) is used to gauge how efficiently resources are converted into outputs. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Total Resolution Time / Resolved Cases, expressed in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Total Resolution Time / Resolved Cases
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 75 (batch 1)
