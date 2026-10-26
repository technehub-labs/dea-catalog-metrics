# dea:metric-query-optimization-cycle-time

Candidate Performance Metric record for **Query Optimization Cycle Time** (QOCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-query-optimization-cycle-time`
- **Name:** Query Optimization Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** QOCT

## 2. Definition

A Database & Data Platform Operations indicator, Query Optimization Cycle Time (QOCT) quantifies how efficiently resources are converted into outputs. It is computed as Days from Slow Query Identified to Optimized, expressed in days. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
Days from Slow Query Identified to Optimized
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3243 (batch 7)
