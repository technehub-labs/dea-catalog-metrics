# dea:metric-cross-sell-ratio

Candidate Performance Metric record for **Cross-Sell Ratio** (XSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cross-sell-ratio`
- **Name:** Cross-Sell Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** XSR

## 2. Definition

Cross-Sell Ratio (XSR) measures growth over time in the Banking & Financial Services domain. It is computed as Products per Customer Relationship, expressed in ratio (x:1 or x). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Financial services.

## 3. Context

Measures the average number of products held per customer in banking relationships. It matters because deeper relationships raise switching costs, share of wallet, and lifetime value. Teams can inflate it by counting dormant or free accounts as products, overstating genuine relationship depth. Read with Share of Wallet and Customer Lifetime Value to check that cross-sold products are actually activated and used.

## Formula

```
Products per Customer Relationship
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 50 (batch 1)
