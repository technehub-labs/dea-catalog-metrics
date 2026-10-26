# dea:metric-passenger-repeat-rate-cruise

Candidate Performance Metric record for **Passenger Repeat Rate (Cruise)** (PRR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passenger-repeat-rate-cruise`
- **Name:** Passenger Repeat Rate (Cruise)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PRR-C

## 2. Definition

Passenger Repeat Rate (Cruise) (PRR-C) measures the retention of customers, users, or assets over time in the Cruise & Passenger Shipping domain. Its calculation is Repeat Passengers / Passengers, measured in percent (%). It originates from and is most used in Hospitality practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of guests who have cruised with the line (or industry) before. Repeat cruisers book cheaper to acquire, spend more onboard, and drive the word-of-mouth engine that fills new ships, so this is the core strategic demand metric for operators. First-timer conversion into repeat is the pipeline that matters most. Read with booking lead time trends and loyalty program participation.

## Formula

```
Repeat Passengers / Passengers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cruise_passenger_shipping
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1924 (batch 6)
