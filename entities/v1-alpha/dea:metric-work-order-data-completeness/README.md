# dea:metric-work-order-data-completeness

Candidate Performance Metric record for **Work Order Data Completeness** (WODC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-work-order-data-completeness`
- **Name:** Work Order Data Completeness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WODC

## 2. Definition

Work Order Data Completeness (WODC) captures the quality of outputs and outcomes for organizations tracking field service & asset performance. It provides the day-to-day signal that a process is running as designed. Its calculation is Work Orders with Complete Asset, Cause, Action Data / Work Orders, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
WODC = Work Orders with Complete Asset, Cause, Action Data / Work Orders
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3395 (batch 7)
