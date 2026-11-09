# dea:metric-turnaround-day-performance

Candidate Performance Metric record for **Turnaround Day Performance** (TDP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-turnaround-day-performance`
- **Name:** Turnaround Day Performance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TDP

## 2. Definition

Turnaround Day Performance (TDP) addresses how efficiently resources are converted into outputs and is a fixture of cruise & passenger shipping reporting. It is computed as Minutes from Last Debarkation to First Embarkation Readiness, expressed in minutes. Its use is concentrated in Hospitality. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
TDP = Minutes from Last Debarkation to First Embarkation Readiness
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cruise_passenger_shipping
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1930 (batch 6)
