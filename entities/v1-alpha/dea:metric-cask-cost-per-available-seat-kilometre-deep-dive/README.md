# dea:metric-cask-cost-per-available-seat-kilometre-deep-dive

Candidate Performance Metric record for **CASK - Cost per Available Seat Kilometre (Deep Dive)** (CASK-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cask-cost-per-available-seat-kilometre-deep-dive`
- **Name:** CASK - Cost per Available Seat Kilometre (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CASK-D

## 2. Definition

CASK - Cost per Available Seat Kilometre (Deep Dive) (CASK-D) addresses how efficiently resources are converted into outputs and is a fixture of airline operations (deep dive) reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Operating Cost / ASK; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. In Airlines, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures unit cost per capacity unit, the cost-side summary of airline operations. CASK discipline is the survival mechanism of low-cost carriers and the restructuring target of full-service ones, and like RASK it needs stage-length and fuel-price decomposition before drawing conclusions. Fuel-hedging and currency effects must be isolated. Read with RASK for the spread and aircraft utilization - Block Hours per Day (Deep Dive) for the capital side.

## Formula

```
Operating Cost / ASK
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2254 (batch 6)
