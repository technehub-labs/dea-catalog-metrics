# dea:metric-truck-turnaround-time

Candidate Performance Metric record for **Truck Turnaround Time** (TTT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-truck-turnaround-time`
- **Name:** Truck Turnaround Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TTT

## 2. Definition

Truck Turnaround Time (TTT) measures how efficiently resources are converted into outputs in the Logistics & Transportation domain. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Hours from Arrival to Departure at Facility, expressed in hours. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Logistics.

## Formula

```
Hours from Arrival to Departure at Facility
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 199 (batch 1)
