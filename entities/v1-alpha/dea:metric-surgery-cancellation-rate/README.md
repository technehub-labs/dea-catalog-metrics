# dea:metric-surgery-cancellation-rate

Candidate Performance Metric record for **Surgery Cancellation Rate** (SCR2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-surgery-cancellation-rate`
- **Name:** Surgery Cancellation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SCR2

## 2. Definition

Surgery Cancellation Rate (SCR2) captures how efficiently resources are converted into outputs for organizations tracking healthcare. It is computed as Cancelled Surgeries / Scheduled Surgeries, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Healthcare.

## 3. Context

Measures the share of scheduled surgeries cancelled on the day or near it. It matters because cancelled surgeries waste expensive operating room capacity and harm patients clinically and emotionally. Gaming risk includes counting cancellations made the day before scheduling as merely rescheduled. Read with Operating Room Utilization and Appointment No-Show Rate to locate whether patients, staffing, or equipment drive cancellations.

## Formula

```
Cancelled Surgeries / Scheduled Surgeries
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 469 (batch 1)
