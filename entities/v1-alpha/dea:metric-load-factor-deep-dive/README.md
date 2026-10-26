# dea:metric-load-factor-deep-dive

Candidate Performance Metric record for **Load Factor (Deep Dive)** (LF-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-load-factor-deep-dive`
- **Name:** Load Factor (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LF-D

## 2. Definition

Load Factor (Deep Dive) (LF-D) captures the utilization or availability of capacity for organizations tracking airline operations (deep dive). It is computed as Revenue Passenger Kilometres / Available Seat Kilometres, expressed in percent (%). Its use is concentrated in Airlines. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of available seats occupied. It is the volume-efficiency metric of airline revenue management: unit costs are spread over filled seats, and load factors below breakeven levels destroy cash regardless of how cheaply seats were sold. High load factors achieved by under-pricing are passenger-full, profit-empty, so read with yield metrics. Read with RASK - Revenue per Available Seat Kilometre (Deep Dive) and break-even load factor.

## Formula

```
Revenue Passenger Kilometres / Available Seat Kilometres
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2252 (batch 6)
