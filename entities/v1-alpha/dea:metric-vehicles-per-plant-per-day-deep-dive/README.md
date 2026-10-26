# dea:metric-vehicles-per-plant-per-day-deep-dive

Candidate Performance Metric record for **Vehicles per Plant per Day (Deep Dive)** (VPD-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vehicles-per-plant-per-day-deep-dive`
- **Name:** Vehicles per Plant per Day (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VPD-D

## 2. Definition

Within Automotive Manufacturing (Deep Dive), Vehicles per Plant per Day (Deep Dive) (VPD-D) is used to gauge the utilization or availability of capacity. Its calculation is Units Produced / Plant Day, measured in count (items per period). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Automotive practice.

## 3. Context

Measures daily production output per assembly plant. It is the throughput heart of automotive manufacturing: plants are enormous fixed-cost machines, and volume against capacity determines unit cost absorption across the entire model range. Output pushed past quality gates converts volume into warranty cost and recall risk. Read with first time through - assembly (Deep Dive) and launch quality index (Deep Dive).

## Formula

```
Units Produced / Plant Day
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2359 (batch 6)
