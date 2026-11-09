# dea:metric-drive-through-service-time

Candidate Performance Metric record for **Drive-Through Service Time** (DSTS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-drive-through-service-time`
- **Name:** Drive-Through Service Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DSTS

## 2. Definition

Drive-Through Service Time (DSTS) addresses how efficiently resources are converted into outputs and is a fixture of restaurants reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Minutes from Order Point to Handoff, expressed in minutes. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Restaurants.

## Formula

```
DSTS = Minutes from Order Point to Handoff
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurants
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 941 (batch 3)
