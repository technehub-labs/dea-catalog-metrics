# dea:metric-aircraft-utilization-block-hours-per-day-deep-dive

Candidate Performance Metric record for **Aircraft Utilization - Block Hours per Day (Deep Dive)** (AUHD-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aircraft-utilization-block-hours-per-day-deep-dive`
- **Name:** Aircraft Utilization - Block Hours per Day (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AUHD-D

## 2. Definition

Within Airline Operations (Deep Dive), Aircraft Utilization - Block Hours per Day (Deep Dive) (AUHD-D) is used to gauge the utilization or availability of capacity. The formula is Block Hours / Aircraft Days - reported in hours. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Airlines sector.

## 3. Context

Measures daily flying hours per aircraft. Utilization is the capital-efficiency core of airline economics: aircraft are the largest owned assets, and spreading ownership cost across more hours is pure margin - provided dispatch reliability and maintenance programs support it. Utilization pushed past maintenance and delay tolerance converts efficiency into cancellation risk. Read with technical dispatch reliability (Deep Dive) and schedule resilience buffer analysis.

## Formula

```
AUHD-D = Block Hours / Aircraft Days
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2251 (batch 6)
