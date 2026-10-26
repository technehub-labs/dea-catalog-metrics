# dea:metric-share-of-wallet

Candidate Performance Metric record for **Share of Wallet** (SOW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-share-of-wallet`
- **Name:** Share of Wallet
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SOW

## 2. Definition

Share of Wallet (SOW) measures growth over time in the Banking & Financial Services domain. Its calculation is Organization Revenue from Customer / Customer Total Spend in Category, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Financial services practice.

## 3. Context

Measures the proportion of a customer's total category spending captured by the institution. It matters because retaining and deepening existing customers is usually far cheaper than acquiring new ones. Estimation is often based on modeled or survey data, so the baseline itself can be quietly adjusted to show growth. Read with Cross-Sell Ratio and Net Revenue Retention to confirm wallet gains translate into actual revenue.

## Formula

```
Organization Revenue from Customer / Customer Total Spend in Category
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 51 (batch 1)
