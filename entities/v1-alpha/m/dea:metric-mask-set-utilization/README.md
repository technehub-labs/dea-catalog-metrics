# dea:metric-mask-set-utilization

Candidate Performance Metric record for **Mask Set Utilization** (MSU-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mask-set-utilization`
- **Name:** Mask Set Utilization
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MSU-S

## 2. Definition

Mask Set Utilization (MSU-S) addresses the utilization or availability of capacity and is a fixture of semiconductor manufacturing (deep dive) reporting. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Active Mask Sets / Mask Sets in Inventory; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. In Semiconductors, it is a recognized element of the standard performance toolkit.

## Formula

```
MSU-S = Active Mask Sets / Mask Sets in Inventory
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_manufacturing_deep_dive
- **Sector:** semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2383 (batch 6)
