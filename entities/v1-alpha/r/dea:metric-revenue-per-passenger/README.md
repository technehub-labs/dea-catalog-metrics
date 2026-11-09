# dea:metric-revenue-per-passenger

Candidate Performance Metric record for **Revenue per Passenger** (RPP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-passenger`
- **Name:** Revenue per Passenger
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPP

## 2. Definition

Revenue per Passenger (RPP) captures the economic value created or preserved for organizations tracking airlines & aviation. The formula is Passenger Revenue / Passengers Carried - reported in currency per unit. It is a standard measure in the Airlines & aviation sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures average revenue carried per passenger, including ancillaries. It matters because it captures fare yield plus ancillary monetization, the two core airline revenue levers. It can be lifted with aggressive ancillary charges that degrade satisfaction and loyalty. Read with Load Factor and Net Promoter Score to confirm revenue growth does not hollow out the experience.

## Formula

```
RPP = Passenger Revenue / Passengers Carried
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 656 (batch 2)
