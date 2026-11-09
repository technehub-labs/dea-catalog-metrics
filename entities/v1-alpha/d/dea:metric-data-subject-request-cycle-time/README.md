# dea:metric-data-subject-request-cycle-time

Candidate Performance Metric record for **Data Subject Request Cycle Time** (DSRCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-subject-request-cycle-time`
- **Name:** Data Subject Request Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DSRCT

## 2. Definition

Data Subject Request Cycle Time (DSRCT) captures how efficiently resources are converted into outputs for organizations tracking data privacy & protection. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Days from Request Received to Fulfilled, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
DSRCT = Days from Request Received to Fulfilled
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_privacy_protection

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3658 (batch 8)
