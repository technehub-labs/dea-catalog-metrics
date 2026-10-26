# dea:metric-foreign-object-detection-rate

Candidate Performance Metric record for **Foreign Object Detection Rate** (FODR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-foreign-object-detection-rate`
- **Name:** Foreign Object Detection Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FODR

## 2. Definition

Within Food & Beverage Manufacturing, Foreign Object Detection Rate (FODR) is used to gauge exposure to adverse outcomes. It is defined as Contaminants Detected by Inspection / Batches; the result is stated in events per thousand or million (scaled). It is a working-level control: thresholds trigger immediate operational response. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. In Food & Beverage, it is a recognized element of the standard performance toolkit.

## Formula

```
Contaminants Detected by Inspection / Batches
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** food_beverage_manufacturing
- **Sector:** food_beverage

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1794 (batch 6)
