# dea:metric-revenue-per-passenger-kilometre

Candidate Performance Metric record for **Revenue per Passenger Kilometre** (RPkM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-passenger-kilometre`
- **Name:** Revenue per Passenger Kilometre
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RPkM

## 2. Definition

Within Rail Transport, Revenue per Passenger Kilometre (RPkM) is used to gauge the economic value created or preserved. Its calculation is Passenger Revenue / Passenger Kilometres, measured in currency per unit. It originates from and is most used in Rail practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Revenue per passenger kilometre divides fare income by distance travelled, and it is the yield metric of rail - the number that shows whether the service is monetizing movement at a sustainable rate. Its dynamics differ by market: regulated fares cap yield on some routes, competing modes (coach, car, air) discipline it on others, and yield management (advance-purchase discounting) trades load factor for yield deliberately. The metric's blind spot is mix: long-distance services yield lower per-km than short commuter trips, so route-mix change moves the number without any pricing action. Read with yield by route type, farebox recovery as the companion, average journey length trend, and yield-versus-occupancy elasticity from pricing experiments.

## Formula

```
Passenger Revenue / Passenger Kilometres
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
- **Domain:** rail_transport
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 994 (batch 3)
