# dea:metric-cost-per-call

Candidate Performance Metric record for **Cost per Call** (CPC-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-call`
- **Name:** Cost per Call
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPC-CC

## 2. Definition

A Contact Center indicator, Cost per Call (CPC-CC) quantifies how efficiently resources are converted into outputs. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Total Contact Center Cost / Calls Handled; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures total contact center cost divided by calls handled. It matters because it is the core unit economics measure for service operations. It can be cut by short-calling, deflection to cheap but poor channels, or offloading work to back-office queues. Read with Average Handle Time trends, First Contact Resolution, and Customer Satisfaction to confirm cost cuts do not buy experience decay.

## Formula

```
Total Contact Center Cost / Calls Handled
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 572 (batch 2)
