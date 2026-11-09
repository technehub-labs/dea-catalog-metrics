# dea:metric-returns-processing-time

Candidate Performance Metric record for **Returns Processing Time** (RPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-returns-processing-time`
- **Name:** Returns Processing Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPT

## 2. Definition

Returns Processing Time (RPT) captures how efficiently resources are converted into outputs for organizations tracking warehousing. Its calculation is Days from Return Receipt to Restock or Disposition, measured in days. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
RPT = Days from Return Receipt to Restock or Disposition
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** warehousing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 216 (batch 1)
