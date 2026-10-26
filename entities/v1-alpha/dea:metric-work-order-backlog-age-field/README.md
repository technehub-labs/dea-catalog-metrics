# dea:metric-work-order-backlog-age-field

Candidate Performance Metric record for **Work Order Backlog Age - Field** (WOBA-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-work-order-backlog-age-field`
- **Name:** Work Order Backlog Age - Field
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WOBA-F

## 2. Definition

A Field Maintenance & Technical Field Service (Deep Dive) indicator, Work Order Backlog Age - Field (WOBA-F) quantifies how efficiently resources are converted into outputs. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Open Field Work Orders beyond Target / Open Orders, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Open Field Work Orders beyond Target / Open Orders
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2908 (batch 7)
