# dea:metric-field-service-response-time-deep-dive

Candidate Performance Metric record for **Field Service Response Time (Deep Dive)** (FSRT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-field-service-response-time-deep-dive`
- **Name:** Field Service Response Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FSRT-D

## 2. Definition

Field Service Response Time (Deep Dive) (FSRT-D) measures how efficiently resources are converted into outputs in the Field Maintenance & Technical Field Service (Deep Dive) domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Hours from Dispatch to On-Site; the result is stated in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Hours from Dispatch to On-Site
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2905 (batch 7)
