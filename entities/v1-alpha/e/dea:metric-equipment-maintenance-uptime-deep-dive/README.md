# dea:metric-equipment-maintenance-uptime-deep-dive

Candidate Performance Metric record for **Equipment Maintenance Uptime (Deep Dive)** (EMU-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-equipment-maintenance-uptime-deep-dive`
- **Name:** Equipment Maintenance Uptime (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EMU-D

## 2. Definition

Equipment Maintenance Uptime (Deep Dive) (EMU-D) captures the utilization or availability of capacity for organizations tracking fitness & wellness (deep dive). It is defined as Equipment Available / Equipment Inventory; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Health & Fitness, it is a recognized element of the standard performance toolkit.

## Formula

```
EMU-D = Equipment Available / Equipment Inventory
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
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** fitness_wellness_deep_dive
- **Sector:** health_fitness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2014 (batch 6)
