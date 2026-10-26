# dea:metric-flight-completion-factor

Candidate Performance Metric record for **Flight Completion Factor** (FCF-AT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-flight-completion-factor`
- **Name:** Flight Completion Factor
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FCF-AT

## 2. Definition

A Airline & Transportation Standard Measures (Deep Dive) indicator, Flight Completion Factor (FCF-AT) quantifies the quality of outputs and outcomes. The formula is Flights Operated / Flights Scheduled - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Airlines & Aviation sector.

## 3. Context

Measures the share of scheduled flights actually operated. Cancellations are the most disruptive airline failure for customers. Completion maintained by extreme delay trades cancellation into OTP erosion. Read with on-time performance rate (Deep Dive) and aircraft daily utilization (Deep Dive).

## Formula

```
Flights Operated / Flights Scheduled
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4280 (batch 10)
