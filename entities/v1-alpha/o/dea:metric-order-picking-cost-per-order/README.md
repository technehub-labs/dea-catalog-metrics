# dea:metric-order-picking-cost-per-order

Candidate Performance Metric record for **Order Picking Cost per Order** (OPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-order-picking-cost-per-order`
- **Name:** Order Picking Cost per Order
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OPC

## 2. Definition

Within Retail & E-commerce, Order Picking Cost per Order (OPC) is used to gauge how efficiently resources are converted into outputs. Its calculation is Total Picking Cost / Orders, measured in currency per unit. It originates from and is most used in Retail practice. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
OPC = Total Picking Cost / Orders
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 502 (batch 1)
