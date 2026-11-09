# dea:metric-engineering-rework-hours-ratio

Candidate Performance Metric record for **Engineering Rework Hours Ratio** (ERHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-engineering-rework-hours-ratio`
- **Name:** Engineering Rework Hours Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ERHR

## 2. Definition

A Engineering & Design indicator, Engineering Rework Hours Ratio (ERHR) quantifies how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Rework Hours / Total Engineering Hours - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ERHR = Rework Hours / Total Engineering Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** engineering_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1769 (batch 6)
