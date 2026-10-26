# dea:metric-mean-time-to-repair-field-assets-deep-dive

Candidate Performance Metric record for **Mean Time to Repair - Field Assets (Deep Dive)** (MTTRF-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-repair-field-assets-deep-dive`
- **Name:** Mean Time to Repair - Field Assets (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MTTRF-D

## 2. Definition

Mean Time to Repair - Field Assets (Deep Dive) (MTTRF-D) captures how efficiently resources are converted into outputs for organizations tracking field maintenance & technical field service (deep dive). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Hours from Fault Report to Functional Restore - reported in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures average time to restore failed customer or company assets serviced in the field. Repair time spans diagnosis, parts logistics, and fix, so it exposes inventory and scheduling weaknesses. MTTR cut by temporary fixes that recur inflates capability. Read with first-time fix rate - field and parts availability fill rate.

## Formula

```
Hours from Fault Report to Functional Restore
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2921 (batch 7)
