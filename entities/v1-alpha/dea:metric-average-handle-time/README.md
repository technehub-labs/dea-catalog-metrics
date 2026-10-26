# dea:metric-average-handle-time

Candidate Performance Metric record for **Average Handle Time** (AHT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-handle-time`
- **Name:** Average Handle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AHT

## 2. Definition

Average Handle Time (AHT) measures how efficiently resources are converted into outputs in the Contact Center domain. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Talk Time + Hold Time + After-Call Work Time / Calls Handled, expressed in minutes. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Talk Time + Hold Time + After-Call Work Time / Calls Handled
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 562 (batch 2)
