# dea:metric-occupancy-rate-cruise

Candidate Performance Metric record for **Occupancy Rate (Cruise)** (ORC-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-occupancy-rate-cruise`
- **Name:** Occupancy Rate (Cruise)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ORC-S

## 2. Definition

Occupancy Rate (Cruise) (ORC-S) addresses the utilization or availability of capacity and is a fixture of cruise & passenger shipping reporting. Its calculation is Passengers / Double Occupancy Berths, measured in percent (%). It originates from and is most used in Hospitality practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures berth capacity sold against capacity available, often above 100 percent with triple and quad occupancy. It is the volume side of cruise yield management, and it is deliberately managed below capacity on new deployments to protect pricing. Occupancy above competitor norm with lower net rates is a red flag on quality of revenue. Read with net revenue per available berth day for the pricing half.

## Formula

```
ORC-S = Passengers / Double Occupancy Berths
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
- **Domain:** cruise_passenger_shipping
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1917 (batch 6)
