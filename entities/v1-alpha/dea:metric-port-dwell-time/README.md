# dea:metric-port-dwell-time

Candidate Performance Metric record for **Port Dwell Time** (PDT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-port-dwell-time`
- **Name:** Port Dwell Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PDT

## 2. Definition

Port Dwell Time (PDT) measures how efficiently resources are converted into outputs in the Maritime & Shipping domain. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Days from Vessel Arrival to Departure, expressed in days. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Maritime & shipping.

## Formula

```
Days from Vessel Arrival to Departure
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 980 (batch 3)
