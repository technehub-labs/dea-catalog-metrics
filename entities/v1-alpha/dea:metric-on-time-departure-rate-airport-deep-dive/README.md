# dea:metric-on-time-departure-rate-airport-deep-dive

Candidate Performance Metric record for **On-Time Departure Rate - Airport (Deep Dive)** (OTDR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-departure-rate-airport-deep-dive`
- **Name:** On-Time Departure Rate - Airport (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OTDR-D

## 2. Definition

Within Airport Operations (Deep Dive), On-Time Departure Rate - Airport (Deep Dive) (OTDR-D) is used to gauge the quality of outputs and outcomes. It is computed as Departures On Time / Departures, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Aviation.

## 3. Context

Measures the share of departing flights pushing back within tolerance. It is the punctuality metric airports control - gate management, boarding support, stand allocation - and it is the input to airline on-time performance that airports are increasingly measured by in service-level agreements. Allocation fairness across airlines matters, since a single dominant carrier's hub timing dominates the average. Read with turnaround resource availability and airline D0 collaboration programs.

## Formula

```
Departures On Time / Departures
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
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2269 (batch 6)
