# dea:metric-baggage-mishandling-rate-per-1-000-passengers-deep-dive

Candidate Performance Metric record for **Baggage Mishandling Rate per 1,000 Passengers (Deep Dive)** (BMR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-baggage-mishandling-rate-per-1-000-passengers-deep-dive`
- **Name:** Baggage Mishandling Rate per 1,000 Passengers (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BMR-D

## 2. Definition

Baggage Mishandling Rate per 1,000 Passengers (Deep Dive) (BMR-D) addresses the quality of outputs and outcomes and is a fixture of airline operations (deep dive) reporting. It is defined as Mishandled Bags / 1,000 Passengers; the result is stated in events per thousand or million (scaled). In Airlines, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures lost, delayed, or damaged bags per thousand passengers. Baggage performance is the most visible operational reliability signal for passengers, drives both compensation cost and repeat-purchase decisions, and it degrades sharply with tight connections and hub congestion. Mishandling must be segmented by station and cause (transfer, loading, tagging), since the transfer hub is usually the choke point. Read with on-time performance (which trades against bag handling) and compensation cost trends.

## Formula

```
BMR-D = Mishandled Bags / 1,000 Passengers
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2263 (batch 6)
