# dea:metric-border-control-processing-time

Candidate Performance Metric record for **Border Control Processing Time** (BCPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-border-control-processing-time`
- **Name:** Border Control Processing Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BCPT

## 2. Definition

A Airport Operations (Deep Dive) indicator, Border Control Processing Time (BCPT) quantifies how efficiently resources are converted into outputs. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Minutes to Process Passenger - reported in minutes. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Aviation sector.

## Formula

```
Minutes to Process Passenger
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2280 (batch 6)
