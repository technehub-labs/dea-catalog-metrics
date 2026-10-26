# dea:metric-aircraft-daily-utilization-deep-dive

Candidate Performance Metric record for **Aircraft Daily Utilization (Deep Dive)** (ADUDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aircraft-daily-utilization-deep-dive`
- **Name:** Aircraft Daily Utilization (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ADUDD

## 2. Definition

Aircraft Daily Utilization (Deep Dive) (ADUDD) measures how efficiently resources are converted into outputs in the Airline & Transportation Standard Measures (Deep Dive) domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Revenue Block Hours / Aircraft Days, expressed in hours. Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Airlines & Aviation.

## 3. Context

Measures revenue hours flown per aircraft per day. Utilization spreads fixed ownership cost, the core of aircraft economics. Utilization pushed past maintenance buffers converts into reliability decay. Read with fleet availability (Transport) (Deep Dive) and maintenance turnaround time.

## Formula

```
Revenue Block Hours / Aircraft Days
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** operations
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** airline_transportation_standard_measures_deep_dive
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4282 (batch 10)
