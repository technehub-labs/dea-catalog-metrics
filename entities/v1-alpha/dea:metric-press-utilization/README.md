# dea:metric-press-utilization

Candidate Performance Metric record for **Press Utilization** (PRU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-press-utilization`
- **Name:** Press Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PRU

## 2. Definition

A Printing & Publishing indicator, Press Utilization (PRU) quantifies the utilization or availability of capacity. It provides the day-to-day signal that a process is running as designed. Its calculation is Press Running Hours / Available Press Hours, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Printing & publishing practice.

## Formula

```
Press Running Hours / Available Press Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** printing_publishing
- **Sector:** printing_publishing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1258 (batch 4)
