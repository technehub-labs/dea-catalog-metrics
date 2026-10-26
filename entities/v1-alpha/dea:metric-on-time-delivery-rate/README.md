# dea:metric-on-time-delivery-rate

Candidate Performance Metric record for **On-Time Delivery Rate** (ODR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-delivery-rate`
- **Name:** On-Time Delivery Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ODR

## 2. Definition

Within Logistics & Transportation, On-Time Delivery Rate (ODR) is used to gauge the quality of outputs and outcomes. The formula is Deliveries On Time / Total Deliveries - reported in percent (%). It is a standard measure in the Logistics sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of shipments delivered by the promised date. It matters because delivery reliability is the promise customers actually remember and reorder on. Gaming risk includes setting easy promised dates or resetting the clock when the customer reschedules. Read with Average Delivery Lead Time and Perfect Order Rate to confirm punctuality coexists with speed and accuracy.

## Formula

```
Deliveries On Time / Total Deliveries
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 194 (batch 1)
