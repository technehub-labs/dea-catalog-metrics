# dea:metric-aircraft-turnaround-time

Candidate Performance Metric record for **Aircraft Turnaround Time** (ATT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aircraft-turnaround-time`
- **Name:** Aircraft Turnaround Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ATT

## 2. Definition

Within Airlines & Aviation, Aircraft Turnaround Time (ATT) is used to gauge how efficiently resources are converted into outputs. It provides the day-to-day signal that a process is running as designed. Its calculation is Minutes from Arrival to Next Departure at Gate, measured in minutes. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Airlines & aviation practice.

## Formula

```
Minutes from Arrival to Next Departure at Gate
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 655 (batch 2)
