# dea:metric-changeover-time

Candidate Performance Metric record for **Changeover Time** (COT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-changeover-time`
- **Name:** Changeover Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** COT

## 2. Definition

Changeover Time (COT) captures how efficiently resources are converted into outputs for organizations tracking operations. It provides the day-to-day signal that a process is running as designed. Its calculation is Time to Switch Production from One Item to Next, measured in minutes. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Time to Switch Production from One Item to Next
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 170 (batch 1)
