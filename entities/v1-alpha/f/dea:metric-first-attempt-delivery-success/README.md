# dea:metric-first-attempt-delivery-success

Candidate Performance Metric record for **First-Attempt Delivery Success** (FADS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-attempt-delivery-success`
- **Name:** First-Attempt Delivery Success
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FADS

## 2. Definition

Within Postal & Courier, First-Attempt Delivery Success (FADS) is used to gauge the quality of outputs and outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Items Delivered on First Attempt / Delivery Attempts - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Postal & courier sector.

## Formula

```
FADS = Items Delivered on First Attempt / Delivery Attempts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** postal_courier
- **Sector:** postal_courier

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 825 (batch 2)
