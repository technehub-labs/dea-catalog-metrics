# dea:metric-andon-pull-rate

Candidate Performance Metric record for **Andon Pull Rate** (APR-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-andon-pull-rate`
- **Name:** Andon Pull Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** APR-A

## 2. Definition

A Automotive Manufacturing (Deep Dive) indicator, Andon Pull Rate (APR-A) quantifies the quality of outputs and outcomes. Its calculation is Line Stops Triggered / Shifts, measured in count (items per period). It originates from and is most used in Automotive practice. It provides the day-to-day signal that a process is running as designed. Values outside the intended band, on either side, warrant investigation.

## Formula

```
APR-A = Line Stops Triggered / Shifts
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2367 (batch 6)
