# dea:metric-peak-demand-staffing-compliance

Candidate Performance Metric record for **Peak Demand Staffing Compliance** (PDSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-peak-demand-staffing-compliance`
- **Name:** Peak Demand Staffing Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PDSC

## 2. Definition

A Workforce Planning & Productivity indicator, Peak Demand Staffing Compliance (PDSC) quantifies the utilization or availability of capacity. Its calculation is Peak Periods Staffed to Model / Peak Periods, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
PDSC = Peak Periods Staffed to Model / Peak Periods
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_productivity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3913 (batch 8)
