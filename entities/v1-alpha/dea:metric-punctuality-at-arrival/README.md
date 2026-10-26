# dea:metric-punctuality-at-arrival

Candidate Performance Metric record for **Punctuality at Arrival** (PAA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-punctuality-at-arrival`
- **Name:** Punctuality at Arrival
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PAA

## 2. Definition

Punctuality at Arrival (PAA) measures the quality of outputs and outcomes in the Airlines & Aviation domain. It is defined as Flights Arriving within Threshold of Schedule / Total Arrivals; the result is stated in percent (%). In Airlines & aviation, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of flights arriving within the punctuality window (the 15-minute convention dominates globally) - the arrival-side punctuality metric, deliberately distinct from departure performance because it is the promise that matters to the passenger: connections, plans, and perception are built on arrival, and departure punctuality is only instrumentally relevant. Its strategic significance is the schedule-integrity measure: arrival performance is the cumulative result of the whole operating day - departure delays, enroute conditions, sequencing, and turnaround health all compound into it - so it is the honest end-state gauge where departure punctuality can look acceptable while arrival deteriorates. The publishing regime matters: aviation regulators and Eurocontrol-type bodies publish arrival punctuality by carrier and airport, which converts the metric into a passenger-facing reputation number and a slot-allocation input at coordinated airports. Read with the cause-mix: air-traffic-flow restrictions versus airline-attributable delay, since the improvement program differs entirely between them.

## Formula

```
Flights Arriving within Threshold of Schedule / Total Arrivals
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 660 (batch 2)
