# dea:metric-on-time-delivery-rate-courier

Candidate Performance Metric record for **On-Time Delivery Rate (Courier)** (ODR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-delivery-rate-courier`
- **Name:** On-Time Delivery Rate (Courier)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ODR-C

## 2. Definition

A Postal & Courier indicator, On-Time Delivery Rate (Courier) (ODR-C) quantifies the quality of outputs and outcomes. The formula is Items Delivered within Service Standard / Items Dispatched - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Postal & courier sector.

## 3. Context

On-time delivery rate for couriers measures parcels delivered within the promised window, and in last-mile logistics the promise has quietly redefined the metric - with e-commerce now competing on same-day and next-day windows, the benchmark is contractual precision rather than best-effort speed. Late parcels drive disproportionate damage: order-level studies consistently show delivery failures are among the top drivers of non-repeat purchase. The metric needs exception-context honesty: weather, peak-season volume surges, and address-quality problems create distinguishable delay classes, and a carrier that cannot decompose its misses cannot fix them. Read with first-attempt success rate (which hides in on-time figures when re-deliveries mask failures), delivery window precision, and customer-confirmed versus carrier-claimed status.

## Formula

```
ODR-C = Items Delivered within Service Standard / Items Dispatched
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** postal_courier
- **Sector:** postal_courier

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 824 (batch 2)
