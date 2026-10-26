# dea:metric-rask-revenue-per-available-seat-kilometre-deep-dive

Candidate Performance Metric record for **RASK - Revenue per Available Seat Kilometre (Deep Dive)** (RASK-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rask-revenue-per-available-seat-kilometre-deep-dive`
- **Name:** RASK - Revenue per Available Seat Kilometre (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RASK-D

## 2. Definition

Within Airline Operations (Deep Dive), RASK - Revenue per Available Seat Kilometre (Deep Dive) (RASK-D) is used to gauge the economic value created or preserved. It is computed as Revenue / ASK, expressed in currency per unit. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Airlines.

## 3. Context

Measures revenue per unit of capacity, the yield-side summary of airline revenue management. RASK moves with load factor, pricing, mix, and stage length together, which is its value and its ambiguity - decomposition is mandatory before concluding anything about pricing health. Short-haul versus long-haul comparisons need stage-length adjustment. Read with CASK - Cost per Available Seat Kilometre (Deep Dive) for the margin spread and load factor (Deep Dive).

## Formula

```
Revenue / ASK
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2253 (batch 6)
