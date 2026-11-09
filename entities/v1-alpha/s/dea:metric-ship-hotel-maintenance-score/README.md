# dea:metric-ship-hotel-maintenance-score

Candidate Performance Metric record for **Ship Hotel Maintenance Score** (SHMS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ship-hotel-maintenance-score`
- **Name:** Ship Hotel Maintenance Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SHMS

## 2. Definition

Ship Hotel Maintenance Score (SHMS) measures the quality of outputs and outcomes in the Cruise & Passenger Shipping domain. Its calculation is Interior Condition Audit Score, measured in score (points). It originates from and is most used in Hospitality practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
SHMS = Interior Condition Audit Score
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cruise_passenger_shipping
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1929 (batch 6)
