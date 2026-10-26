# dea:metric-maintenance-work-order-backlog-hotels

Candidate Performance Metric record for **Maintenance Work Order Backlog (Hotels)** (MWOB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintenance-work-order-backlog-hotels`
- **Name:** Maintenance Work Order Backlog (Hotels)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MWOB

## 2. Definition

Maintenance Work Order Backlog (Hotels) (MWOB) captures exposure to adverse outcomes for organizations tracking hotel & resort operations (deep dive). Its calculation is Open Work Orders / Rooms, measured in ratio (x:1 or x). It originates from and is most used in Hospitality practice. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Open Work Orders / Rooms
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** hotel_resort_operations_deep_dive
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1913 (batch 6)
