# dea:metric-average-delivery-lead-time

Candidate Performance Metric record for **Average Delivery Lead Time** (ADLT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-delivery-lead-time`
- **Name:** Average Delivery Lead Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ADLT

## 2. Definition

Average Delivery Lead Time (ADLT) measures how efficiently resources are converted into outputs in the Logistics & Transportation domain. It is defined as Days from Dispatch to Delivery; the result is stated in days. In Logistics, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures mean elapsed time from order dispatch to customer delivery. It matters because it is the customer-felt speed metric for delivery promises and e-commerce competitiveness. It can be gamed by measuring only from dispatch rather than order, or averaging only completed easy deliveries. Read with On-Time Delivery Rate and Order Fulfillment Cycle Time to pair speed with reliability.

## Formula

```
Days from Dispatch to Delivery
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 202 (batch 1)
