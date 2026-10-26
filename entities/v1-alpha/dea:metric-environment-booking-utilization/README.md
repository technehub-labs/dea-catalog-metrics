# dea:metric-environment-booking-utilization

Candidate Performance Metric record for **Environment Booking Utilization** (EBU-RM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-environment-booking-utilization`
- **Name:** Environment Booking Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EBU-RM

## 2. Definition

Within Release Management & Environments, Environment Booking Utilization (EBU-RM) is used to gauge the utilization or availability of capacity. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Booked Environment Hours / Available Hours, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Booked Environment Hours / Available Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** release_management_environments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2735 (batch 7)
