# dea:metric-workload-balance-index

Candidate Performance Metric record for **Workload Balance Index** (WBI-WF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workload-balance-index`
- **Name:** Workload Balance Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WBI-WF

## 2. Definition

A Workforce Planning & Productivity indicator, Workload Balance Index (WBI-WF) quantifies how efficiently resources are converted into outputs. Its calculation is Distribution Variance of Load across Comparable Roles, measured in index (0-100 or normalized). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Distribution Variance of Load across Comparable Roles
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_productivity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3912 (batch 8)
