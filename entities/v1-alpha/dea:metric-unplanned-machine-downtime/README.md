# dea:metric-unplanned-machine-downtime

Candidate Performance Metric record for **Unplanned Machine Downtime** (UMD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unplanned-machine-downtime`
- **Name:** Unplanned Machine Downtime
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UMD

## 2. Definition

Unplanned Machine Downtime (UMD) addresses exposure to adverse outcomes and is a fixture of manufacturing reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Unplanned Downtime Events or Hours per Period, measured in hours. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Manufacturing practice.

## Formula

```
Unplanned Downtime Events or Hours per Period
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 254 (batch 1)
