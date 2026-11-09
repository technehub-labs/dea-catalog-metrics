# dea:metric-cross-sell-ratio-products-per-customer

Candidate Performance Metric record for **Cross-Sell Ratio (Products per Customer)** (XSR-B) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cross-sell-ratio-products-per-customer`
- **Name:** Cross-Sell Ratio (Products per Customer)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** XSR-B

## 2. Definition

Cross-Sell Ratio (Products per Customer) (XSR-B) addresses growth over time and is a fixture of retail banking & lending reporting. It is computed as Products Held / Customer Relationships, expressed in ratio (x:1 or x). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Banking.

## 3. Context

Measures average product count per retail banking customer. It matters because multi-product relationships raise retention and lifetime value. Counting dormant or fee-waived accounts inflates the ratio without economic substance. Read with Share of Wallet and Active Product Usage Rate to confirm depth is real.

## Formula

```
XSR-B = Products Held / Customer Relationships
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 842 (batch 3)
