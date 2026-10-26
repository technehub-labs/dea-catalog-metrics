# dea:metric-shrinkage

Candidate Performance Metric record for **Shrinkage** (SHK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shrinkage`
- **Name:** Shrinkage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SHK

## 2. Definition

Shrinkage (SHK) captures the utilization or availability of capacity for organizations tracking contact center. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Non-Productive Time / Total Paid Time, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SHK = Non-Productive Time / Total Paid Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 574 (batch 2)
