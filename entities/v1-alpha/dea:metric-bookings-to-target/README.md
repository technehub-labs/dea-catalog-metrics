# dea:metric-bookings-to-target

Candidate Performance Metric record for **Bookings to Target** (B2T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bookings-to-target`
- **Name:** Bookings to Target
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** B2T

## 2. Definition

Bookings to Target (B2T) measures conformance to standards, plans, or obligations in the Sales domain. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Total Bookings / Target Bookings; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures total bookings against the period target. It matters as the single clearest statement of commercial execution for the period. Gaming risk includes end-of-period discounting and multi-year deals booked entirely upfront to cross the line. Read with Forecast Accuracy and Revenue Recognition (or Deferred Revenue trends) to see whether bookings quality matches bookings quantity.

## Formula

```
Total Bookings / Target Bookings
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 103 (batch 1)
