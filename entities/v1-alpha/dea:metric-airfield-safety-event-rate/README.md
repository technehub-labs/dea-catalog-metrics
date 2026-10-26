# dea:metric-airfield-safety-event-rate

Candidate Performance Metric record for **Airfield Safety Event Rate** (ASER-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-airfield-safety-event-rate`
- **Name:** Airfield Safety Event Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ASER-A

## 2. Definition

Airfield Safety Event Rate (ASER-A) addresses exposure to adverse outcomes and is a fixture of airport operations (deep dive) reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Runway Incursions or Excursions per 100,000 Movements; the result is stated in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. In Aviation, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures runway incursions, taxiway excursions, and airside events against movements. Airside safety is the license-to-operate core of airports - a single serious incursion can dominate the regulatory relationship for years - and the rate is the leading indicator before an accident forces attention. Reporting culture matters as much as incidence: suppressed near-miss reporting is the classic pre-accident signature. Read with runway incursion severity distribution and airside-driving compliance.

## Formula

```
Runway Incursions or Excursions per 100,000 Movements
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2278 (batch 6)
