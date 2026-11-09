# dea:metric-mean-time-to-respond-field

Candidate Performance Metric record for **Mean Time to Respond (Field)** (MTTR-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-respond-field`
- **Name:** Mean Time to Respond (Field)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTTR-F

## 2. Definition

A Field Service & Asset Performance indicator, Mean Time to Respond (Field) (MTTR-F) quantifies how efficiently resources are converted into outputs. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Time from Dispatch to Technician Arrival - reported in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
MTTR-F = Time from Dispatch to Technician Arrival
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** operations
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3380 (batch 7)
