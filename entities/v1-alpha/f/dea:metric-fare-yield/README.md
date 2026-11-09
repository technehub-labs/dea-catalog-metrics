# dea:metric-fare-yield

Candidate Performance Metric record for **Fare Yield** (FY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fare-yield`
- **Name:** Fare Yield
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FY

## 2. Definition

Fare Yield (FY) captures the economic value created or preserved for organizations tracking airlines & aviation. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Passenger Revenue / Revenue Passenger Kilometres - reported in currency per unit. Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Airlines & aviation sector.

## 3. Context

Passenger revenue per revenue passenger-kilometre - the pricing metric of aviation, measuring what the airline earns for each kilometre a paying passenger actually travels, and the number that separates airlines earning premium economics from those flying volume. Its strategic significance is the pricing-power read: yield trends against market show whether the airline's product and network earn above-market pricing, and yield decompositions (by cabin, by route, by booking class) are how revenue management examines its own steering. The companion logic is strict: yield means nothing without load factor, since high yield on empty aircraft is a pricing strategy with no revenue - which is why the two are always presented as a pair and their product is RASK. Read with the distance effect: short-haul yields run structurally higher than long-haul (fixed costs spread over fewer kilometres), so yield comparisons need stage-adjustment to be honest.

## Formula

```
FY = Passenger Revenue / Revenue Passenger Kilometres
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 658 (batch 2)
