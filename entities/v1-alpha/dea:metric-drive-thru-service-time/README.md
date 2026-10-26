# dea:metric-drive-thru-service-time

Candidate Performance Metric record for **Drive-Thru Service Time** (DTST) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-drive-thru-service-time`
- **Name:** Drive-Thru Service Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DTST

## 2. Definition

Drive-Thru Service Time (DTST) captures how efficiently resources are converted into outputs for organizations tracking restaurant operations (deep dive). It is computed as Minutes from Order to Hand-Off, expressed in minutes. Its use is concentrated in Restaurants. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
DTST = Minutes from Order to Hand-Off
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
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurant_operations_deep_dive
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2350 (batch 6)
