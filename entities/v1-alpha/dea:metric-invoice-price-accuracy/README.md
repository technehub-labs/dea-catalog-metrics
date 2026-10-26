# dea:metric-invoice-price-accuracy

Candidate Performance Metric record for **Invoice Price Accuracy** (IPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-invoice-price-accuracy`
- **Name:** Invoice Price Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IPA

## 2. Definition

Invoice Price Accuracy (IPA) measures the quality of outputs and outcomes in the Pricing & Revenue Management domain. The formula is Invoices Billed at Approved Price / Invoices - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Invoices Billed at Approved Price / Invoices
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1072 (batch 4)
