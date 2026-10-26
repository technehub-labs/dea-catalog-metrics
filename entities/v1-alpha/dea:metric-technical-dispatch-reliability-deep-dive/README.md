# dea:metric-technical-dispatch-reliability-deep-dive

Candidate Performance Metric record for **Technical Dispatch Reliability (Deep Dive)** (TDR-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-technical-dispatch-reliability-deep-dive`
- **Name:** Technical Dispatch Reliability (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TDR-A

## 2. Definition

Within Airline Operations (Deep Dive), Technical Dispatch Reliability (Deep Dive) (TDR-A) is used to gauge the quality of outputs and outcomes. It is defined as Departures without Technical Delay or Cancel / Departures; the result is stated in percent (%). In Airlines, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of departures without technical delays, cancellations, or mechanical returns. It is the fleet-health metric of airline engineering: dispatch reliability compounds into schedule integrity, crew utilization, and customer trust, and it is the leading indicator of an aging or strained fleet. Reliability managed by deferring non-critical defects must be read with the deferred-defect backlog. Read with maintenance-related cancellation rate and fleet age (Deep Dive).

## Formula

```
Departures without Technical Delay or Cancel / Departures
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2256 (batch 6)
