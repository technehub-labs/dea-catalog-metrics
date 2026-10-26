# dea:metric-returns-handling-cycle-time

Candidate Performance Metric record for **Returns Handling Cycle Time** (RHCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-returns-handling-cycle-time`
- **Name:** Returns Handling Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RHCT

## 2. Definition

Returns Handling Cycle Time (RHCT) addresses how efficiently resources are converted into outputs and is a fixture of postal & courier reporting. Its calculation is Days from Return Receipt to Disposition, measured in days. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Postal & courier practice.

## Formula

```
Days from Return Receipt to Disposition
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** postal_courier
- **Sector:** postal_courier

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 833 (batch 2)
