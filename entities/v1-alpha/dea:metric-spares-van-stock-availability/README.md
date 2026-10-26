# dea:metric-spares-van-stock-availability

Candidate Performance Metric record for **Spares Van Stock Availability** (SVSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-spares-van-stock-availability`
- **Name:** Spares Van Stock Availability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SVSA

## 2. Definition

Within Telecom Field & Installation, Spares Van Stock Availability (SVSA) is used to gauge the utilization or availability of capacity. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Jobs Completed without Spares Stockout / Jobs, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Telecommunications.

## Formula

```
Jobs Completed without Spares Stockout / Jobs
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** telecom_field_installation
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1283 (batch 5)
