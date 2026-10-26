# dea:metric-seat-turnover-per-service

Candidate Performance Metric record for **Seat Turnover per Service** (STPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-seat-turnover-per-service`
- **Name:** Seat Turnover per Service
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** STPS

## 2. Definition

A Restaurants indicator, Seat Turnover per Service (STPS) quantifies the utilization or availability of capacity. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Guests Served / Seats per Service Period, expressed in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Restaurants.

## Formula

```
Guests Served / Seats per Service Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurants
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 938 (batch 3)
