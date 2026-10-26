# dea:metric-passenger-load-factor

Candidate Performance Metric record for **Passenger Load Factor** (PLF-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passenger-load-factor`
- **Name:** Passenger Load Factor
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PLF-A

## 2. Definition

Passenger Load Factor (PLF-A) captures the utilization or availability of capacity for organizations tracking airlines & aviation. The formula is Revenue Passenger Kilometres / Available Seat Kilometres - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Airlines & aviation sector.

## 3. Context

Revenue passenger-kilometres as a share of available seat-kilometres - the capacity-utilization metric of commercial aviation, and the hinge of airline economics: the marginal cost of carrying an additional passenger is near zero, so almost all revenue past break-even load factor falls to profit, and conversely every empty seat carries the full cost of the flight that carried it. Its strategic significance is the yield-trade it pairs with: load factor bought with low fares is volume without economics, which is why it is always read with yield and their product (revenue per available seat-kilometre) is the number that matters. Read with the network dimension: load factor systemwide hides the route variance that matters - the strong routes subsidizing the weak ones - and route-level load factor against competitor frequency is where capacity decisions are actually made. The seasonality is structural: airlines operate summer and holiday peaks against shoulder troughs, so year-on-year same-period comparison is the only honest trend.

## Formula

```
Revenue Passenger Kilometres / Available Seat Kilometres
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 646 (batch 2)
