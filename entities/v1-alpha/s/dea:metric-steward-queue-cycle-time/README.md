# dea:metric-steward-queue-cycle-time

Candidate Performance Metric record for **Steward Queue Cycle Time** (SQCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-steward-queue-cycle-time`
- **Name:** Steward Queue Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SQCT

## 2. Definition

Steward Queue Cycle Time (SQCT) measures how efficiently resources are converted into outputs in the Master Data Management domain. It is computed as Days for Steward to Resolve Data Curation Queue Items, expressed in days. It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
SQCT = Days for Steward to Resolve Data Curation Queue Items
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3643 (batch 8)
