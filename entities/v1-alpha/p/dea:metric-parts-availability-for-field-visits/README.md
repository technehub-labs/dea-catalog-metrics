# dea:metric-parts-availability-for-field-visits

Candidate Performance Metric record for **Parts Availability for Field Visits** (PAFFV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-parts-availability-for-field-visits`
- **Name:** Parts Availability for Field Visits
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PAFFV

## 2. Definition

Within Field Maintenance & Technical Field Service (Deep Dive), Parts Availability for Field Visits (PAFFV) is used to gauge the utilization or availability of capacity. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Jobs Completed without Parts Stockout / Jobs, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
PAFFV = Jobs Completed without Parts Stockout / Jobs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2911 (batch 7)
