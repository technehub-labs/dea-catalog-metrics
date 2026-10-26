# dea:metric-schedule-integrity-rate

Candidate Performance Metric record for **Schedule Integrity Rate** (SIR-AT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-schedule-integrity-rate`
- **Name:** Schedule Integrity Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SIR-AT

## 2. Definition

Schedule Integrity Rate (SIR-AT) measures the quality of outputs and outcomes in the Airline & Transportation Standard Measures (Deep Dive) domain. It is defined as Flights Departing as Scheduled without Swap or Cancel / Flights; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Airlines & Aviation, it is a recognized element of the standard performance toolkit.

## Formula

```
SIR-AT = Flights Departing as Scheduled without Swap or Cancel / Flights
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** airline_transportation_standard_measures_deep_dive
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4288 (batch 10)
