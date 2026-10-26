# dea:metric-plant-load-factor

Candidate Performance Metric record for **Plant Load Factor** (PLF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-plant-load-factor`
- **Name:** Plant Load Factor
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PLF

## 2. Definition

Within Energy & Utilities, Plant Load Factor (PLF) is used to gauge the utilization or availability of capacity. It is defined as Actual Energy Generated / Maximum Possible Generation; the result is stated in percent (%). In Energy & utilities, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Actual energy generated as a share of what the plant could generate at full capacity over the period - the utilization metric of power generation, and the hinge of plant economics: fixed costs are recovered only across generated megawatt-hours, so a load factor collapsing from high to low takes a plant from profit to loss without any change in spending. Its strategic significance has been transformed by the energy transition: renewable-heavy grids push thermal plants from baseload to intermittent operation, their load factors falling structurally, which is the economic fact behind retirements, capacity-market design, and stranded-asset debates. Read with the price context: low load factor at high marginal prices (peaking duty) can be more profitable than high load factor at depressed prices, which is why this metric is always read with capture price, not alone.

## Formula

```
Actual Energy Generated / Maximum Possible Generation
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 439 (batch 1)
