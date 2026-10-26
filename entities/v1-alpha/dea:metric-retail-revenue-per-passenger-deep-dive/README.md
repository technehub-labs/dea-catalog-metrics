# dea:metric-retail-revenue-per-passenger-deep-dive

Candidate Performance Metric record for **Retail Revenue per Passenger (Deep Dive)** (RRPP-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-retail-revenue-per-passenger-deep-dive`
- **Name:** Retail Revenue per Passenger (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRPP-D

## 2. Definition

A Airport Operations (Deep Dive) indicator, Retail Revenue per Passenger (Deep Dive) (RRPP-D) quantifies the economic value created or preserved. The formula is Concession Revenue / Passengers - reported in currency per unit. It is a standard measure in the Aviation sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures non-aeronautical commercial revenue per passenger. Concessions are the profit engine of airport economics - aeronautical fees are regulated and thin, retail is not - so per-passenger yield drives the multiple the airport trades on. Spend per passenger must be read with dwell time and passenger mix (transfer versus origin), since these are structural levers beyond concession quality. Read with passenger satisfaction index - Airport (Deep Dive) and concession occupancy rates.

## Formula

```
Concession Revenue / Passengers
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
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2277 (batch 6)
