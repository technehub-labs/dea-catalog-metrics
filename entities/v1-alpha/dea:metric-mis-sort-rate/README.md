# dea:metric-mis-sort-rate

Candidate Performance Metric record for **Mis-sort Rate** (MSR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mis-sort-rate`
- **Name:** Mis-sort Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MSR-P

## 2. Definition

Within Postal & Courier, Mis-sort Rate (MSR-P) is used to gauge the quality of outputs and outcomes. It is defined as Incorrectly Sorted Items / Items Sorted; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Postal & courier, it is a recognized element of the standard performance toolkit.

## Formula

```
Incorrectly Sorted Items / Items Sorted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** postal_courier
- **Sector:** postal_courier

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 827 (batch 2)
