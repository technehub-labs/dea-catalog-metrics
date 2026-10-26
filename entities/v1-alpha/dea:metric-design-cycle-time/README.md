# dea:metric-design-cycle-time

Candidate Performance Metric record for **Design Cycle Time** (DCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-design-cycle-time`
- **Name:** Design Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DCT

## 2. Definition

A R&D and Innovation indicator, Design Cycle Time (DCT) quantifies how efficiently resources are converted into outputs. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Days from Design Brief to Design Freeze, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures elapsed time from concept to design freeze for a new product or release. It matters because development speed determines time to market and iteration capacity. Teams can cut it cosmetically by freezing designs before requirements are stable, pushing churn downstream. Read with Requirements Change Rate and Rework Rate to confirm faster cycles are not just earlier handoffs.

## Formula

```
Days from Design Brief to Design Freeze
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** r_d_and_innovation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 545 (batch 1)
