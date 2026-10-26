# dea:metric-crew-induced-delay-rate

Candidate Performance Metric record for **Crew-Induced Delay Rate** (CIDR-AT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crew-induced-delay-rate`
- **Name:** Crew-Induced Delay Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CIDR-AT

## 2. Definition

Crew-Induced Delay Rate (CIDR-AT) addresses exposure to adverse outcomes and is a fixture of airline & transportation standard measures (deep dive) reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Delays Attributed to Crew Availability / Departure Delays, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Airlines & Aviation practice.

## Formula

```
Delays Attributed to Crew Availability / Departure Delays
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4284 (batch 10)
