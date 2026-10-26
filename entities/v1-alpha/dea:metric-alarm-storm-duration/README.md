# dea:metric-alarm-storm-duration

Candidate Performance Metric record for **Alarm Storm Duration** (ASD-NOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alarm-storm-duration`
- **Name:** Alarm Storm Duration
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ASD-NOC

## 2. Definition

A Network Operations Center (Deep Dive) indicator, Alarm Storm Duration (ASD-NOC) quantifies exposure to adverse outcomes. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Minutes of Correlated Alert Flooding per Storm Event, expressed in minutes. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Minutes of Correlated Alert Flooding per Storm Event
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2855 (batch 7)
