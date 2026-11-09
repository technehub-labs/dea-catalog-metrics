# dea:metric-data-restoration-success-rate

Candidate Performance Metric record for **Data Restoration Success Rate** (DRSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-restoration-success-rate`
- **Name:** Data Restoration Success Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DRSR

## 2. Definition

Within Business Continuity & Disaster Recovery, Data Restoration Success Rate (DRSR) is used to gauge exposure to adverse outcomes. Its calculation is Restores Verified Complete and Correct / Restore Attempts, measured in percent (%). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
DRSR = Restores Verified Complete and Correct / Restore Attempts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_continuity_disaster_recovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3528 (batch 8)
