# dea:metric-commission-per-transaction

Candidate Performance Metric record for **Commission per Transaction** (CPTX) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-commission-per-transaction`
- **Name:** Commission per Transaction
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPTX

## 2. Definition

Within Real Estate Brokerage, Commission per Transaction (CPTX) is used to gauge the economic value created or preserved. It is computed as Total Commission Revenue / Closed Transactions, expressed in currency value. It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Real estate.

## 3. Context

Measures average commission revenue per closed transaction. It matters because it links agent effort to brokerage economics and price-band mix. Low-price high-volume strategies can hide declining commission health behind transaction counts. Read with Average Sale Price trends and Agent Productivity (Transactions) to interpret unit economics correctly.

## Formula

```
CPTX = Total Commission Revenue / Closed Transactions
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
- **Domain:** real_estate_brokerage
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1014 (batch 3)
