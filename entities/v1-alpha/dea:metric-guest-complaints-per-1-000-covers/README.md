# dea:metric-guest-complaints-per-1-000-covers

Candidate Performance Metric record for **Guest Complaints per 1,000 Covers** (GCPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guest-complaints-per-1-000-covers`
- **Name:** Guest Complaints per 1,000 Covers
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GCPC

## 2. Definition

Within Restaurants, Guest Complaints per 1,000 Covers (GCPC) is used to gauge the quality of outputs and outcomes. It is computed as Complaints / Covers Served x 1,000, expressed in events per thousand or million (scaled). Its use is concentrated in Restaurants. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Complaints / Covers Served x 1,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 942 (batch 3)
