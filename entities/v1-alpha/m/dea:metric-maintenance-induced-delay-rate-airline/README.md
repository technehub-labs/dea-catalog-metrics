# dea:metric-maintenance-induced-delay-rate-airline

Candidate Performance Metric record for **Maintenance-Induced Delay Rate (Airline)** (MIDRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintenance-induced-delay-rate-airline`
- **Name:** Maintenance-Induced Delay Rate (Airline)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MIDRA

## 2. Definition

Maintenance-Induced Delay Rate (Airline) (MIDRA) addresses exposure to adverse outcomes and is a fixture of airline & transportation standard measures (deep dive) reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Delays Attributed to Maintenance / Departure Delays, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Airlines & Aviation.

## Formula

```
MIDRA = Delays Attributed to Maintenance / Departure Delays
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** airline_transportation_standard_measures_deep_dive
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4285 (batch 10)
