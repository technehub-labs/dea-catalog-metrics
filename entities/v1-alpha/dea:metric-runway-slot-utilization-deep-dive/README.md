# dea:metric-runway-slot-utilization-deep-dive

Candidate Performance Metric record for **Runway Slot Utilization (Deep Dive)** (RSU-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-runway-slot-utilization-deep-dive`
- **Name:** Runway Slot Utilization (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RSU-D

## 2. Definition

Runway Slot Utilization (Deep Dive) (RSU-D) addresses the utilization or availability of capacity and is a fixture of airport operations (deep dive) reporting. Its calculation is Used Slots / Declared Capacity, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Aviation practice.

## 3. Context

Measures use of declared runway capacity against slot allocations. Slot capacity is the scarce asset of congested airports, and utilization integrity - measured use, not allocated-then-unused - determines both actual throughput and regulatory position in slot-allocation regimes. Use-it-or-lose-it rules make parked slots a compliance exposure. Read with declared-capacity methodology changes and weather-normalized throughput trends.

## Formula

```
Used Slots / Declared Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2274 (batch 6)
