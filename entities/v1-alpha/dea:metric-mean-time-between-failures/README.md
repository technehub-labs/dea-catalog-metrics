# dea:metric-mean-time-between-failures

Candidate Performance Metric record for **Mean Time Between Failures** (MTBF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-between-failures`
- **Name:** Mean Time Between Failures
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTBF

## 2. Definition

A Operations indicator, Mean Time Between Failures (MTBF) quantifies exposure to adverse outcomes. Its calculation is Total Operating Time / Number of Failures, measured in hours. It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Total Operating Time / Number of Failures
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 169 (batch 1)
