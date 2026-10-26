# dea:metric-backlog-aging-gbs

Candidate Performance Metric record for **Backlog Aging (GBS)** (BAG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-backlog-aging-gbs`
- **Name:** Backlog Aging (GBS)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BAG

## 2. Definition

Within Shared Services & Global Business Services, Backlog Aging (GBS) (BAG) is used to gauge the utilization or availability of capacity. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Open Requests Older than Target Resolution Age, expressed in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
BAG = Open Requests Older than Target Resolution Age
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** shared_services_global_business_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1060 (batch 4)
