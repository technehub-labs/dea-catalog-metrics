# dea:metric-appointment-no-show-rate

Candidate Performance Metric record for **Appointment No-Show Rate** (NSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-appointment-no-show-rate`
- **Name:** Appointment No-Show Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NSR

## 2. Definition

A Healthcare indicator, Appointment No-Show Rate (NSR) quantifies how efficiently resources are converted into outputs. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Missed Appointments / Scheduled Appointments; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Healthcare, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of scheduled patient appointments missed without notice. It matters because no-shows waste clinical capacity, delay care, and signal access or engagement problems. Providers can cut it by overbooking aggressively, which trades no-shows into longer waits. Read with Patient Wait Time and Rescheduling patterns to confirm reductions reflect better engagement, not statistical masking.

## Formula

```
Missed Appointments / Scheduled Appointments
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 472 (batch 1)
