# dea:metric-ad-fill-rate

Candidate Performance Metric record for **Ad Fill Rate** (AFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ad-fill-rate`
- **Name:** Ad Fill Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AFR

## 2. Definition

Ad Fill Rate (AFR) measures the utilization or availability of capacity in the Media & Entertainment domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Ads Delivered / Ad Slots Available; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Media & entertainment, it is a recognized element of the standard performance toolkit.

## Formula

```
Ads Delivered / Ad Slots Available
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
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** media_entertainment
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 697 (batch 2)
