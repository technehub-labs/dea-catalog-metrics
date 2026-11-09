# dea:metric-units-per-transaction

Candidate Performance Metric record for **Units per Transaction** (UPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-units-per-transaction`
- **Name:** Units per Transaction
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UPT

## 2. Definition

Units per Transaction (UPT) measures the economic value created or preserved in the Retail & E-commerce domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Units Sold / Number of Transactions, expressed in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Retail.

## 3. Context

Measures average item count per customer transaction. It matters because attach rate and multi-item baskets are the operating levers of retail basket economics. Cross-selling low-margin fillers can lift units while diluting profit. Read with Average Transaction Value and Sell-Through Rate to check that more units means more profitable baskets.

## Formula

```
UPT = Units Sold / Number of Transactions
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 488 (batch 1)
