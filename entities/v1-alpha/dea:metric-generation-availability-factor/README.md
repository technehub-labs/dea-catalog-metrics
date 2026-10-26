# dea:metric-generation-availability-factor

Candidate Performance Metric record for **Generation Availability Factor** (GAF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-generation-availability-factor`
- **Name:** Generation Availability Factor
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GAF

## 2. Definition

A Energy & Utilities indicator, Generation Availability Factor (GAF) quantifies the utilization or availability of capacity. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Available Generation Hours / Calendar Hours; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Energy & utilities, it is a recognized element of the standard performance toolkit.

## 3. Context

The share of time a generating unit is available to generate, excluding outages - the reliability metric of the plant fleet, and the hinge of capacity value: in capacity markets, units are compensated for being available when the system needs them, and availability shortfalls convert directly to revenue loss and penalties. Its strategic content is the planned-versus-unplanned split: planned outages (maintenance, overhauls) are scheduled economics with known cost, while unplanned forced outages are reliability failures whose cost includes the market price of replacement power - and the forced-outage rate is the number that separates disciplined operators from struggling assets in every fleet benchmarking study. Read with the duration-weighted view: a few long forced outages damage the number - and the operator's reputation with the system operator - more than many brief trips, and the aging-fleet pattern of rising forced-outage frequency is the standard leading indicator of retirement decisions.

## Formula

```
Available Generation Hours / Calendar Hours
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 445 (batch 1)
