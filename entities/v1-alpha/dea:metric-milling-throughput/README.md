# dea:metric-milling-throughput

Candidate Performance Metric record for **Milling Throughput** (MTH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-milling-throughput`
- **Name:** Milling Throughput
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MTH

## 2. Definition

Milling Throughput (MTH) measures the utilization or availability of capacity in the Mining & Metals domain. It is defined as Ore Milled per Period; the result is stated in tonnes. It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Mining & metals, it is a recognized element of the standard performance toolkit.

## Formula

```
Ore Milled per Period
```

## Unit

- **Unit reference:** `dea:unit-tonnes`
- **Unit:** tonnes
- **Unit label (as published):** tonnes

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** mining_metals
- **Sector:** mining_metals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 717 (batch 2)
