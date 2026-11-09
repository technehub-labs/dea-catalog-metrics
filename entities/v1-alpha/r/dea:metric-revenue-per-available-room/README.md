# dea:metric-revenue-per-available-room

Candidate Performance Metric record for **Revenue per Available Room** (RevPAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-available-room`
- **Name:** Revenue per Available Room
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RevPAR

## 2. Definition

A Hospitality & Food Service indicator, Revenue per Available Room (RevPAR) quantifies the economic value created or preserved. Its calculation is Room Revenue / Rooms Available, measured in currency value. It originates from and is most used in Hospitality practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Room revenue divided by available rooms - the product of occupancy and average daily rate, and the single number that resolves their trade-off: the hotel that fills by discounting and the hotel that holds rate while standing empty both lose, and RevPAR is the arbiter. Its strategic significance is the universal benchmark: hotel performance comparison, brand health, and asset valuation conventionally operate on RevPAR (per available room, not per occupied), because it prices the capacity the hotel actually owns. Read the two components separately whenever it moves: RevPAR growth from occupancy is share-driven and cyclical, growth from rate is pricing-power-driven and more durable, and the same headline number can mean opposite things. The refinement the industry adds is RevPAR index - RevPAR relative to a competitive set - which converts the absolute number into the market-position question that owners actually ask.

## Formula

```
RevPAR = Room Revenue / Rooms Available
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** hospitality_food_service
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 506 (batch 1)
