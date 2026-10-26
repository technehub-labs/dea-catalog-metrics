# dea:metric-aircraft-parking-stand-turnover

Candidate Performance Metric record for **Aircraft Parking Stand Turnover** (APST) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aircraft-parking-stand-turnover`
- **Name:** Aircraft Parking Stand Turnover
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APST

## 2. Definition

A Airport Operations (Deep Dive) indicator, Aircraft Parking Stand Turnover (APST) quantifies the utilization or availability of capacity. Its calculation is Stand Occupancy Hours / Stand Hours Available, measured in percent (%). It originates from and is most used in Aviation practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Stand Occupancy Hours / Stand Hours Available
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2281 (batch 6)
