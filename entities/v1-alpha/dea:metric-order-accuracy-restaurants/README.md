# dea:metric-order-accuracy-restaurants

Candidate Performance Metric record for **Order Accuracy (Restaurants)** (OAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-order-accuracy-restaurants`
- **Name:** Order Accuracy (Restaurants)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OAR

## 2. Definition

Order Accuracy (Restaurants) (OAR) addresses the quality of outputs and outcomes and is a fixture of restaurants reporting. It is computed as Orders Delivered as Placed / Orders, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Restaurants.

## Formula

```
Orders Delivered as Placed / Orders
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurants
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 943 (batch 3)
