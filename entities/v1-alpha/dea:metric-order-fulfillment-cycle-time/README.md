# dea:metric-order-fulfillment-cycle-time

Candidate Performance Metric record for **Order Fulfillment Cycle Time** (OFCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-order-fulfillment-cycle-time`
- **Name:** Order Fulfillment Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OFCT

## 2. Definition

Within Operations, Order Fulfillment Cycle Time (OFCT) is used to gauge how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Days from Order Received to Customer Delivery - reported in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures elapsed time from customer order to delivery. It matters because it is the customer-felt speed metric that drives satisfaction and repeat purchases. It can be gamed by starting the clock at shipment rather than order receipt, or quoting only easy urban orders. Read with On-Time Delivery Rate and Perfect Order Rate to confirm speed is not coming at the cost of reliability.

## Formula

```
Days from Order Received to Customer Delivery
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 159 (batch 1)
