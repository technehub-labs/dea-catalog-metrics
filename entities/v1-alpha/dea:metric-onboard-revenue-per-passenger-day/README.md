# dea:metric-onboard-revenue-per-passenger-day

Candidate Performance Metric record for **Onboard Revenue per Passenger Day** (ORPD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-onboard-revenue-per-passenger-day`
- **Name:** Onboard Revenue per Passenger Day
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ORPD

## 2. Definition

A Cruise & Passenger Shipping indicator, Onboard Revenue per Passenger Day (ORPD) quantifies the economic value created or preserved. It is computed as Onboard Spend / Passenger Days, expressed in currency per unit. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Hospitality.

## 3. Context

Measures spending on drinks, casino, spa, excursions, and specialty dining per guest per day. Onboard revenue carries much higher margin than ticket revenue, making this the profitability driver of modern cruise economics. Excursion margin varies with owned-versus-partnered mix, so read composition alongside the rate. Read with pre-cruise booking share (cheaper to serve) and passenger mix effects.

## Formula

```
Onboard Spend / Passenger Days
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
- **Domain:** cruise_passenger_shipping
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1919 (batch 6)
