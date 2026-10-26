# dea:metric-revenue-per-available-seat-kilometre

Candidate Performance Metric record for **Revenue per Available Seat Kilometre** (RASK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-available-seat-kilometre`
- **Name:** Revenue per Available Seat Kilometre
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RASK

## 2. Definition

Within Airlines & Aviation, Revenue per Available Seat Kilometre (RASK) is used to gauge the economic value created or preserved. Its calculation is Passenger Revenue / Available Seat Kilometres, measured in currency per unit. It originates from and is most used in Airlines & aviation practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Revenue divided by available seat-kilometres - the unit-revenue metric of aviation, and the product of load factor and yield: it measures what a seat-kilometre of capacity actually earns, regardless of whether the revenue came from filling more seats or charging more for them. Its strategic significance is the pricing-power indicator it provides: RASK movements against the market reveal whether the airline is earning more per unit of capacity than peers - the premium-traffic and network-quality signal - and RASK trends across the industry are the pricing-cycle gauge that airline analysts track most closely. The honest read decomposes before acting: RASK rising on load factor (filling seats) and RASK rising on yield (pricing harder) have different durability and different competitive meaning, and the split is the analysis. Read with CASK: the RASK-CASK spread is the airline's entire margin arithmetic in two numbers, which is why the pairing is the industry's core benchmark table.

## Formula

```
Passenger Revenue / Available Seat Kilometres
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 649 (batch 2)
