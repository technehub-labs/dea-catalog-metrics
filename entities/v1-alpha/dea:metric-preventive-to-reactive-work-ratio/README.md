# dea:metric-preventive-to-reactive-work-ratio

Candidate Performance Metric record for **Preventive-to-Reactive Work Ratio** (PRWR-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-preventive-to-reactive-work-ratio`
- **Name:** Preventive-to-Reactive Work Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRWR-F

## 2. Definition

Preventive-to-Reactive Work Ratio (PRWR-F) addresses exposure to adverse outcomes and is a fixture of field service & asset performance reporting. It is computed as PM Work Orders / Reactive Work Orders, expressed in ratio (x:1 or x). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
PRWR-F = PM Work Orders / Reactive Work Orders
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** operations
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3383 (batch 7)
