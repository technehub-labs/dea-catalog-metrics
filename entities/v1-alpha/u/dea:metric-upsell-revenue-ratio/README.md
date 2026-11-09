# dea:metric-upsell-revenue-ratio

Candidate Performance Metric record for **Upsell Revenue Ratio** (UPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-upsell-revenue-ratio`
- **Name:** Upsell Revenue Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UPR

## 2. Definition

Within Sales, Upsell Revenue Ratio (UPR) is used to gauge growth over time. It is defined as Upsell and Cross-Sell Revenue / Total Revenue; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of revenue from upgrades, add-ons, or expansions of existing customers. It matters because expansion revenue is the cheapest growth and validates delivered value. Gaming risk includes reclassifying renewals with inflationary uplift as upsell, overstating true expansion. Read with Net Revenue Retention and Churn Rate to confirm the installed base is genuinely deepening.

## Formula

```
UPR = Upsell and Cross-Sell Revenue / Total Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 97 (batch 1)
