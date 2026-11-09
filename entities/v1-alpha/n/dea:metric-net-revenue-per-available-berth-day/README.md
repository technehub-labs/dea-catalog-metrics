# dea:metric-net-revenue-per-available-berth-day

Candidate Performance Metric record for **Net Revenue per Available Berth Day** (NRABD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-revenue-per-available-berth-day`
- **Name:** Net Revenue per Available Berth Day
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NRABD

## 2. Definition

Net Revenue per Available Berth Day (NRABD) captures the economic value created or preserved for organizations tracking cruise & passenger shipping. It is computed as Net Revenue / Available Berth Days, expressed in currency per unit. Its use is concentrated in Hospitality. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures cruise net revenue (cabin revenue net of commissions, discounts, and onboard allocations) per available berth day. It is the industry-standard yield metric, letting operators compare performance across ship sizes and itineraries. Netting conventions vary, so standardize before benchmarking peers. Read with onboard revenue per passenger day for the total revenue picture.

## Formula

```
NRABD = Net Revenue / Available Berth Days
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1918 (batch 6)
