# dea:metric-first-attempt-delivery-rate-deep-dive

Candidate Performance Metric record for **First Attempt Delivery Rate (Deep Dive)** (FADR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-attempt-delivery-rate-deep-dive`
- **Name:** First Attempt Delivery Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FADR-D

## 2. Definition

A Parcel & Last-Mile Logistics (Deep Dive) indicator, First Attempt Delivery Rate (Deep Dive) (FADR-D) quantifies the quality of outputs and outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Deliveries on First Attempt / Delivery Attempts, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Logistics & Trade.

## 3. Context

Measures parcels delivered on the first attempt without redirection or failed drop. It is the cost and experience hinge of last-mile logistics: every failed attempt doubles the delivery cost and generates the customer contact that erodes loyalty, and e-commerce repeat purchase correlates strongly with first-attempt success. Receiver availability data (delivery windows, safe-place options) moves the rate more than driver effort. Read with customer delivery window compliance and cost per parcel (Deep Dive).

## Formula

```
FADR-D = Deliveries on First Attempt / Delivery Attempts
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
- **Domain:** parcel_last_mile_logistics_deep_dive
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2330 (batch 6)
