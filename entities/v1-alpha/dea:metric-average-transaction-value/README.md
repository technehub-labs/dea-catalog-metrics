# dea:metric-average-transaction-value

Candidate Performance Metric record for **Average Transaction Value** (ATV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-transaction-value`
- **Name:** Average Transaction Value
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ATV

## 2. Definition

Within Retail & E-commerce, Average Transaction Value (ATV) is used to gauge the economic value created or preserved. It is defined as Total Revenue / Number of Transactions; the result is stated in currency value. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Retail, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures mean revenue per completed transaction in retail or e-commerce. It matters because raising basket size is usually cheaper than raising traffic. It can be gamed by discount bundles that lift value while crushing margin. Read with Units per Transaction and Gross Margin trends to confirm higher baskets carry profitable mix, not just discounted volume.

## Formula

```
Total Revenue / Number of Transactions
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 487 (batch 1)
