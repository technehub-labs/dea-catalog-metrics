# dea:metric-available-seat-kilometres

Candidate Performance Metric record for **Available Seat Kilometres** (ASK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-available-seat-kilometres`
- **Name:** Available Seat Kilometres
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ASK

## 2. Definition

Available Seat Kilometres (ASK) addresses the utilization or availability of capacity and is a fixture of airlines & aviation reporting. Its calculation is Seats Flown x Distance Flown, measured in count (items per period). It originates from and is most used in Airlines & aviation practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Seats flown multiplied by distance - the capacity metric of aviation, and the denominator of nearly everything in airline economics: load factor, unit revenue, and unit cost are all expressed per ASK, which is what makes airlines of different sizes and network shapes comparable at all. Its strategic significance is the supply decision it records: ASK growth is capacity deployment - where the airline placed its bets on routes and aircraft - and capacity growth against demand growth is the primary determinant of industry pricing, which is why ASK trends are watched as the competitive-supply signal in every market analysis. Read with gauge and stage decomposition: the same ASK growth from adding widebody long-haul and from adding regional short-haul frequency are entirely different strategic statements, and the aggregate hides which. The ASK framework is also the honesty layer for cost: cost per ASK (CASK) is the industry's universal efficiency currency.

## Formula

```
Seats Flown x Distance Flown
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 648 (batch 2)
