# dea:metric-aircraft-utilization

Candidate Performance Metric record for **Aircraft Utilization** (ACU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aircraft-utilization`
- **Name:** Aircraft Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACU

## 2. Definition

A Airlines & Aviation indicator, Aircraft Utilization (ACU) quantifies the utilization or availability of capacity. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Block Hours Flown / Aircraft Days Available; the result is stated in hours. Improvement means raising this figure toward best-in-class levels. In Airlines & aviation, it is a recognized element of the standard performance toolkit.

## 3. Context

Hours flown (or block hours operated) per aircraft per day - the asset-productivity metric of the airline fleet, and the strategic one: aircraft are enormous capital assets whose ownership cost runs around the clock, so utilization is the primary diluter of fixed cost per flight - and the structural difference between low-cost and full-service models is in large part a utilization philosophy, with the low-cost tradition built on fast turnarounds and long daily hours. Its significance is the compounding with seat density and load factor: utilization times seats times load factor times yield is the revenue-day of the asset, and every improvement in utilization multiplies through. The honest read is against maintenance reality: utilization pushed past maintenance-planning capacity produces the reliability deterioration that returns it, so the sustainable-utilization frontier is what the metric actually manages toward. Read with fleet-type honesty, since different aircraft types carry different natural utilization ceilings.

## Formula

```
Block Hours Flown / Aircraft Days Available
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 651 (batch 2)
