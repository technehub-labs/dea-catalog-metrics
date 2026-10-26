# dea:metric-rake-dwell-time-at-sidings-deep-dive

Candidate Performance Metric record for **Rake Dwell Time at Sidings (Deep Dive)** (RDT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rake-dwell-time-at-sidings-deep-dive`
- **Name:** Rake Dwell Time at Sidings (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RDT-D

## 2. Definition

A Rail Freight (Deep Dive) indicator, Rake Dwell Time at Sidings (Deep Dive) (RDT-D) quantifies how efficiently resources are converted into outputs. It provides the day-to-day signal that a process is running as designed. Its calculation is Hours at Sidings per Trip, measured in hours. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Rail practice.

## Formula

```
Hours at Sidings per Trip
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2423 (batch 6)
