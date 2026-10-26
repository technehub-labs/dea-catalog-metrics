# dea:metric-scheduled-work-order-compliance

Candidate Performance Metric record for **Scheduled Work Order Compliance** (SWOC-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scheduled-work-order-compliance`
- **Name:** Scheduled Work Order Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SWOC-F

## 2. Definition

Scheduled Work Order Compliance (SWOC-F) captures conformance to standards, plans, or obligations for organizations tracking field service & asset performance. Its calculation is PM Work Orders Completed on Schedule / Scheduled, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
SWOC-F = PM Work Orders Completed on Schedule / Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3384 (batch 7)
