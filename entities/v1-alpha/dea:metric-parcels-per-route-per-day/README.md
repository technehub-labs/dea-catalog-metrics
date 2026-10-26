# dea:metric-parcels-per-route-per-day

Candidate Performance Metric record for **Parcels per Route per Day** (PPRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-parcels-per-route-per-day`
- **Name:** Parcels per Route per Day
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PPRD

## 2. Definition

Parcels per Route per Day (PPRD) addresses the utilization or availability of capacity and is a fixture of postal & courier reporting. Its calculation is Parcels Delivered / Route Days, measured in ratio (x:1 or x). It originates from and is most used in Postal & courier practice. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Parcels Delivered / Route Days
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 826 (batch 2)
