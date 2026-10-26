# dea:metric-class-utilization

Candidate Performance Metric record for **Class Utilization** (CLU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-class-utilization`
- **Name:** Class Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CLU

## 2. Definition

Class Utilization (CLU) captures the utilization or availability of capacity for organizations tracking fitness & wellness. It is computed as Attendees / Class Capacity, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Fitness & wellness.

## Formula

```
Attendees / Class Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** fitness_wellness
- **Sector:** fitness_wellness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1032 (batch 3)
