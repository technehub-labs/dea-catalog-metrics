# dea:metric-customer-delivery-window-compliance

Candidate Performance Metric record for **Customer Delivery Window Compliance** (CDWC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-delivery-window-compliance`
- **Name:** Customer Delivery Window Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDWC

## 2. Definition

Within Parcel & Last-Mile Logistics (Deep Dive), Customer Delivery Window Compliance (CDWC) is used to gauge the quality of outputs and outcomes. Its calculation is Deliveries within Promised Window / Deliveries, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Logistics & Trade practice.

## 3. Context

Measures deliveries within the promised or customer-selected window. It is the promise-keeping metric of last-mile service: customers forgive slower delivery promised honestly more readily than fast delivery missed, and window compliance drives both repeat purchase and contact-center volume. Overly wide windows flatter the metric while degrading the offer, so window width belongs in the read. Read with first attempt delivery rate (Deep Dive) and complaint themes.

## Formula

```
CDWC = Deliveries within Promised Window / Deliveries
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2341 (batch 6)
