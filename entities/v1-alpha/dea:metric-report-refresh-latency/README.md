# dea:metric-report-refresh-latency

Candidate Performance Metric record for **Report Refresh Latency** (RRL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-report-refresh-latency`
- **Name:** Report Refresh Latency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRL

## 2. Definition

A Data Management & Analytics indicator, Report Refresh Latency (RRL) quantifies how efficiently resources are converted into outputs. Its calculation is Time from Source Update to Dashboard Availability, measured in hours. It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Time from Source Update to Dashboard Availability
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 341 (batch 1)
