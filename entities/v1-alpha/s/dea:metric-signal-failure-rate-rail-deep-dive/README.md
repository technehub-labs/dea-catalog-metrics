# dea:metric-signal-failure-rate-rail-deep-dive

Candidate Performance Metric record for **Signal Failure Rate (Rail Deep Dive)** (SFR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-signal-failure-rate-rail-deep-dive`
- **Name:** Signal Failure Rate (Rail Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SFR-D

## 2. Definition

A Rail Freight (Deep Dive) indicator, Signal Failure Rate (Rail Deep Dive) (SFR-D) quantifies exposure to adverse outcomes. Its calculation is Failures per 1,000 Signals, measured in events per thousand or million (scaled). It originates from and is most used in Rail practice. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
SFR-D = Failures per 1,000 Signals
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2429 (batch 6)
