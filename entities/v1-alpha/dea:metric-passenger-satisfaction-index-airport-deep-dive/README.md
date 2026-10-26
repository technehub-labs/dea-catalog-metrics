# dea:metric-passenger-satisfaction-index-airport-deep-dive

Candidate Performance Metric record for **Passenger Satisfaction Index - Airport (Deep Dive)** (PSIA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passenger-satisfaction-index-airport-deep-dive`
- **Name:** Passenger Satisfaction Index - Airport (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PSIA-D

## 2. Definition

Within Airport Operations (Deep Dive), Passenger Satisfaction Index - Airport (Deep Dive) (PSIA-D) is used to gauge the engagement or satisfaction of the people involved. Its calculation is Composite Airport Survey Score, measured in index (0-100 or normalized). It originates from and is most used in Aviation practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures overall passenger sentiment across the airport journey (check-in, security, wayfinding, dwell). It is the commercial flywheel of airports: satisfied passengers dwell longer and spend more retail, and satisfaction data directs capital allocation among competing improvements. Segment by passenger type and terminal, since averages obscure the experience failures that drive complaints. Read with security wait-time distribution and retail revenue per passenger (Deep Dive).

## Formula

```
Composite Airport Survey Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2276 (batch 6)
