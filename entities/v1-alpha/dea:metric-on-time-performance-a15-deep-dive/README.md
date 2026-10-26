# dea:metric-on-time-performance-a15-deep-dive

Candidate Performance Metric record for **On-Time Performance - A15 (Deep Dive)** (OTP-A15) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-performance-a15-deep-dive`
- **Name:** On-Time Performance - A15 (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OTP-A15

## 2. Definition

On-Time Performance - A15 (Deep Dive) (OTP-A15) addresses the quality of outputs and outcomes and is a fixture of airline operations (deep dive) reporting. It is computed as Arrivals within 15 Minutes / Arrivals, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Airlines.

## 3. Context

Measures flights arriving within fifteen minutes of schedule, the industry-standard OTP definition. A15 is the customer-felt punctuality metric and the one that gates slot allocations and compensation regimes in many jurisdictions. A15 gains from schedule padding are real for passengers but mask operational decline, so read alongside D0. Read with air traffic control delay allocations and turnaround root-cause analysis.

## Formula

```
OTP-A15 = Arrivals within 15 Minutes / Arrivals
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2250 (batch 6)
