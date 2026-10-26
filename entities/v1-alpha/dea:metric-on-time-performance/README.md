# dea:metric-on-time-performance

Candidate Performance Metric record for **On-Time Performance** (OTP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-performance`
- **Name:** On-Time Performance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OTP

## 2. Definition

A Airlines & Aviation indicator, On-Time Performance (OTP) quantifies the quality of outputs and outcomes. The formula is Flights Departing within Threshold of Schedule / Total Flights - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Airlines & aviation sector.

## 3. Context

The share of flights departing or arriving within the regulatory window (conventionally fifteen minutes for arrival in the US regime) - the punctuality metric that aviation regulators publish by airline and airport, and the one passengers experience as the airline's basic honesty. Its strategic significance is three-fold: regulatory (persistent poor performance attracts enforcement and slot consequences at capacity-constrained airports), commercial (punctuality drives passenger choice and corporate-contract eligibility), and financial (delay is a direct operating cost - crew time, fuel, passenger reaccommodation - that airlines measure per minute). The honest read separates controllable from uncontrollable: weather and air-traffic-control delays are environment, while late-arriving aircraft cascades and turnaround delays are the operation - and attribution regimes exist precisely because the metric is only actionable decomposed. Read with the cancellation companion, since punctuality improved by cancelling the worst flights converts delay into a different form of disruption that the OTP figure never shows.

## Formula

```
Flights Departing within Threshold of Schedule / Total Flights
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 647 (batch 2)
