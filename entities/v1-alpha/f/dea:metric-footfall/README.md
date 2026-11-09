# dea:metric-footfall

Candidate Performance Metric record for **Footfall** (FF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-footfall`
- **Name:** Footfall
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FF

## 2. Definition

Within Retail & E-commerce, Footfall (FF) is used to gauge the utilization or availability of capacity. Its calculation is Customer Visits per Period, measured in count (items per period). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Retail practice.

## Formula

```
FF = Customer Visits per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 490 (batch 1)
