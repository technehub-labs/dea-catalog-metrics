# dea:metric-backup-success-rate-deep-dive

Candidate Performance Metric record for **Backup Success Rate (Deep Dive)** (BKPSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-backup-success-rate-deep-dive`
- **Name:** Backup Success Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BKPSR

## 2. Definition

A Database & Data Platform Operations indicator, Backup Success Rate (Deep Dive) (BKPSR) quantifies exposure to adverse outcomes. It is defined as Successful Backups / Scheduled Backups; the result is stated in percent (%). In Software, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Successful Backups / Scheduled Backups
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3229 (batch 7)
