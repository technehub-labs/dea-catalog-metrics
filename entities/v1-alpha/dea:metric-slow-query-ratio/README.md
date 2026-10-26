# dea:metric-slow-query-ratio

Candidate Performance Metric record for **Slow Query Ratio** (SQR-DB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-slow-query-ratio`
- **Name:** Slow Query Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SQR-DB

## 2. Definition

Within Database & Data Platform Operations, Slow Query Ratio (SQR-DB) is used to gauge the quality of outputs and outcomes. It is defined as Queries Exceeding Latency Budget / Total Queries; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
Queries Exceeding Latency Budget / Total Queries
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3227 (batch 7)
