# dea:metric-passenger-throughput-per-gate-hour

Candidate Performance Metric record for **Passenger Throughput per Gate Hour** (PTGH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passenger-throughput-per-gate-hour`
- **Name:** Passenger Throughput per Gate Hour
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PTGH

## 2. Definition

Within Airport Operations (Deep Dive), Passenger Throughput per Gate Hour (PTGH) is used to gauge the utilization or availability of capacity. It is computed as Passengers / Gate Hours, expressed in count (items per period). Its use is concentrated in Aviation. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Passengers / Gate Hours
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2270 (batch 6)
