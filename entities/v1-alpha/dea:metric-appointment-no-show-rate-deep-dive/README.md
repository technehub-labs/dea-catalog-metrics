# dea:metric-appointment-no-show-rate-deep-dive

Candidate Performance Metric record for **Appointment No-Show Rate (Deep Dive)** (ANSR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-appointment-no-show-rate-deep-dive`
- **Name:** Appointment No-Show Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ANSR-D

## 2. Definition

Appointment No-Show Rate (Deep Dive) (ANSR-D) measures how efficiently resources are converted into outputs in the Medical Practice & Clinical Operations domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Missed Appointments without Cancellation / Scheduled, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Healthcare practice.

## Formula

```
Missed Appointments without Cancellation / Scheduled
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1632 (batch 6)
