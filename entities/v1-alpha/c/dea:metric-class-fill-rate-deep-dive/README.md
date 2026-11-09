# dea:metric-class-fill-rate-deep-dive

Candidate Performance Metric record for **Class Fill Rate (Deep Dive)** (CFR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-class-fill-rate-deep-dive`
- **Name:** Class Fill Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CFR-D

## 2. Definition

A Fitness & Wellness (Deep Dive) indicator, Class Fill Rate (Deep Dive) (CFR-D) quantifies the utilization or availability of capacity. It is computed as Booked Spots / Available Class Spots, expressed in percent (%). Its use is concentrated in Health & Fitness. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
CFR-D = Booked Spots / Available Class Spots
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** fitness_wellness_deep_dive
- **Sector:** health_fitness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2012 (batch 6)
