# dea:metric-collision-rate-per-million-miles

Candidate Performance Metric record for **Collision Rate per Million Miles** (CRPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-collision-rate-per-million-miles`
- **Name:** Collision Rate per Million Miles
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CRPM

## 2. Definition

Collision Rate per Million Miles (CRPM) addresses exposure to adverse outcomes and is a fixture of public transit reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Collisions / Miles Operated x 1,000,000, measured in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Public transit practice.

## 3. Context

Collision rate per million miles measures safety performance normalized for exposure, and it is the transit metric that regulators audit and insurers price - collisions are the events that erode public confidence, drive claims cost, and for transit operators, injure the passengers they exist to serve. The denominator discipline matters: revenue-miles versus vehicle-miles versus passenger-miles measure different things, and collision definitions (reportable versus preventable versus chargeable) vary across agencies, making cross-agency benchmarking treacherous. Preventable-collision analysis is the management tool: distinguishing collisions the operator could have avoided through technique changes training exposure. Read with collision cause distribution (rear-end and pedestrian strikes dominate bus operations), preventable rate trend, operator-tenure correlation, and near-miss reporting which provides leading-indicator volume.

## Formula

```
Collisions / Miles Operated x 1,000,000
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1007 (batch 3)
