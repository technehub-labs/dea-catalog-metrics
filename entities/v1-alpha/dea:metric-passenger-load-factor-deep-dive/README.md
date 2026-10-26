# dea:metric-passenger-load-factor-deep-dive

Candidate Performance Metric record for **Passenger Load Factor (Deep Dive)** (PLFDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passenger-load-factor-deep-dive`
- **Name:** Passenger Load Factor (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PLFDD

## 2. Definition

Passenger Load Factor (Deep Dive) (PLFDD) measures how efficiently resources are converted into outputs in the Airline & Transportation Standard Measures (Deep Dive) domain. It is defined as Revenue Passenger Kilometers / Available Seat Kilometers; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Airlines & Aviation, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of available seats sold. Load factor is the core unit-economics lever of airline profitability. Load bought with deep discounting fills seats while destroying yield. Read with revenue per available seat kilometer and break-even load factor (Airline).

## Formula

```
Revenue Passenger Kilometers / Available Seat Kilometers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** airline_transportation_standard_measures_deep_dive
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4275 (batch 10)
