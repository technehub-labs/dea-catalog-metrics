# dea:metric-slot-utilization-liner-deep-dive

Candidate Performance Metric record for **Slot Utilization - Liner (Deep Dive)** (SUL-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-slot-utilization-liner-deep-dive`
- **Name:** Slot Utilization - Liner (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SUL-D

## 2. Definition

Slot Utilization - Liner (Deep Dive) (SUL-D) measures the utilization or availability of capacity in the Maritime Shipping (Deep Dive) domain. It is defined as TEU Carried / TEU Capacity; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Maritime, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of vessel slot capacity actually utilized. Slot utilization is the break-even arithmetic of container shipping: vessels carry enormous fixed cost whether full or empty, and utilization swings decide quarterly profitability for entire alliances. Utilization bought at freight rates below variable cost is volume for its own sake. Read with freight-rate trends on the same lanes and empty-repositioning cost.

## Formula

```
SUL-D = TEU Carried / TEU Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2435 (batch 6)
