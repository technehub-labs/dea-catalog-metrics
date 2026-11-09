# dea:metric-complaint-handling-cycle-time

Candidate Performance Metric record for **Complaint Handling Cycle Time** (CHCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-complaint-handling-cycle-time`
- **Name:** Complaint Handling Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CHCT

## 2. Definition

Complaint Handling Cycle Time (CHCT) measures conformance to standards, plans, or obligations in the Medical Devices domain. Its calculation is Days from Complaint Receipt to Closure, measured in days. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. It originates from and is most used in Medical devices practice.

## 3. Context

Measures time from medical device complaint receipt to closure. It matters because complaint timelines are regulated, and slow handling delays hazard detection. Teams can close complaints administratively pending investigation, stopping the clock without resolving. Read with Complaint Trend analysis and Adverse Event reporting timeliness to confirm closure means adjudicated.

## Formula

```
CHCT = Days from Complaint Receipt to Closure
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_devices
- **Sector:** medical_devices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 756 (batch 2)
