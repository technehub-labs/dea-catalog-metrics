# dea:metric-break-even-load-factor-airline

Candidate Performance Metric record for **Break-Even Load Factor (Airline)** (BELF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-break-even-load-factor-airline`
- **Name:** Break-Even Load Factor (Airline)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BELF

## 2. Definition

Break-Even Load Factor (Airline) (BELF) measures exposure to adverse outcomes in the Airline & Transportation Standard Measures (Deep Dive) domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Operating Cost per ASK / Revenue per ASK; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Airlines & Aviation, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the load factor required to cover operating costs. The spread between break-even and actual load factor is the profit cushion. Break-even computed on peak-season yields understates annual pressure. Read with passenger load factor (Deep Dive) and revenue per available seat kilometer.

## Formula

```
Operating Cost per ASK / Revenue per ASK
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** airline_transportation_standard_measures_deep_dive
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4278 (batch 10)
