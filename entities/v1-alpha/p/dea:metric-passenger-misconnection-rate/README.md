# dea:metric-passenger-misconnection-rate

Candidate Performance Metric record for **Passenger Misconnection Rate** (PMR-AT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passenger-misconnection-rate`
- **Name:** Passenger Misconnection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PMR-AT

## 2. Definition

Within Airline & Transportation Standard Measures (Deep Dive), Passenger Misconnection Rate (PMR-AT) is used to gauge the quality of outputs and outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Passengers Missing Connections due to Own Airline Delay / Connecting Passengers, measured in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Airlines & Aviation practice.

## Formula

```
PMR-AT = Passengers Missing Connections due to Own Airline Delay / Connecting Passengers
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** operations
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4283 (batch 10)
