# dea:metric-backlog-of-aged-cases

Candidate Performance Metric record for **Backlog of Aged Cases** (BAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-backlog-of-aged-cases`
- **Name:** Backlog of Aged Cases
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BAC

## 2. Definition

Backlog of Aged Cases (BAC) measures the utilization or availability of capacity in the Customer domain. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Open Cases Older than Threshold Age, expressed in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
BAC = Open Cases Older than Threshold Age
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 83 (batch 1)
