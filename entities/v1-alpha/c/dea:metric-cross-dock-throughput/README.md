# dea:metric-cross-dock-throughput

Candidate Performance Metric record for **Cross-Dock Throughput** (CDT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cross-dock-throughput`
- **Name:** Cross-Dock Throughput
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDT

## 2. Definition

Within Warehousing, Cross-Dock Throughput (CDT) is used to gauge the utilization or availability of capacity. It is computed as Units Cross-Docked / Day, expressed in count (items per period). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
CDT = Units Cross-Docked / Day
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** warehousing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 219 (batch 1)
