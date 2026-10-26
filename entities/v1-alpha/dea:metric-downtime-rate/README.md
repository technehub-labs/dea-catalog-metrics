# dea:metric-downtime-rate

Candidate Performance Metric record for **Downtime Rate** (DTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-downtime-rate`
- **Name:** Downtime Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DTR

## 2. Definition

Downtime Rate (DTR) captures the utilization or availability of capacity for organizations tracking operations. Its calculation is Downtime Hours / Scheduled Operating Hours, measured in percent (%). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
DTR = Downtime Hours / Scheduled Operating Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 167 (batch 1)
