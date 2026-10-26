# dea:metric-baggage-handling-system-availability-deep-dive

Candidate Performance Metric record for **Baggage Handling System Availability (Deep Dive)** (BHSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-baggage-handling-system-availability-deep-dive`
- **Name:** Baggage Handling System Availability (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BHSA

## 2. Definition

Baggage Handling System Availability (Deep Dive) (BHSA) addresses the utilization or availability of capacity and is a fixture of airport operations (deep dive) reporting. It is computed as BHS Available Time / Required Time, expressed in percent (%). Its use is concentrated in Aviation. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
BHS Available Time / Required Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2273 (batch 6)
