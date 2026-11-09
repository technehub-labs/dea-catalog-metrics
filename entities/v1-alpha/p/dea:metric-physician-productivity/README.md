# dea:metric-physician-productivity

Candidate Performance Metric record for **Physician Productivity** (PP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-physician-productivity`
- **Name:** Physician Productivity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PP

## 2. Definition

Within Healthcare, Physician Productivity (PP) is used to gauge how efficiently resources are converted into outputs. It is defined as Relative Value Units Generated per Physician; the result is stated in ratio (x:1 or x). In Healthcare, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures clinical output per physician, typically visits, procedures, or work relative value units. It matters because physician labor is the largest clinical cost and a capacity bottleneck. Chasing productivity can push shorter visits that degrade care quality and satisfaction. Read with Patient Satisfaction and Referral patterns to ensure throughput gains do not cost care quality.

## Formula

```
PP = Relative Value Units Generated per Physician
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 476 (batch 1)
