# dea:metric-table-turnover-rate

Candidate Performance Metric record for **Table Turnover Rate** (TTR-H) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-table-turnover-rate`
- **Name:** Table Turnover Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TTR-H

## 2. Definition

Table Turnover Rate (TTR-H) measures the utilization or availability of capacity in the Hospitality & Food Service domain. Its calculation is Table Service Cycles / Table per Service Period, measured in ratio (x:1 or x). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Hospitality practice.

## Formula

```
Table Service Cycles / Table per Service Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** hospitality_food_service
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 508 (batch 1)
