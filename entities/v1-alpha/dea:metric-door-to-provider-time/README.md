# dea:metric-door-to-provider-time

Candidate Performance Metric record for **Door-to-Provider Time** (D2PT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-door-to-provider-time`
- **Name:** Door-to-Provider Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** D2PT

## 2. Definition

Door-to-Provider Time (D2PT) addresses how efficiently resources are converted into outputs and is a fixture of healthcare quality & patient safety standard measures reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Minutes from ED Arrival to First Provider Contact, measured in minutes. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Healthcare practice.

## Formula

```
Minutes from ED Arrival to First Provider Contact
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4245 (batch 10)
