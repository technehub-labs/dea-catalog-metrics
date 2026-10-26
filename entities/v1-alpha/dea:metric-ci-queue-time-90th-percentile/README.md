# dea:metric-ci-queue-time-90th-percentile

Candidate Performance Metric record for **CI Queue Time - 90th Percentile** (CIQT90) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ci-queue-time-90th-percentile`
- **Name:** CI Queue Time - 90th Percentile
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CIQT90

## 2. Definition

A Continuous Integration indicator, CI Queue Time - 90th Percentile (CIQT90) quantifies the utilization or availability of capacity. Its calculation is Minutes Waiting in Build Queue, measured in minutes. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Minutes Waiting in Build Queue
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2678 (batch 7)
