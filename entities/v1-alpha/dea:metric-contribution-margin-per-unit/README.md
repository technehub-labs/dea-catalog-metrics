# dea:metric-contribution-margin-per-unit

Candidate Performance Metric record for **Contribution Margin per Unit** (CMU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contribution-margin-per-unit`
- **Name:** Contribution Margin per Unit
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CMU

## 2. Definition

Within Product Costing & Margin Management, Contribution Margin per Unit (CMU) is used to gauge the economic value created or preserved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Price per Unit - Variable Cost per Unit, measured in currency per unit. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the selling price of a single unit minus its variable cost, exposing how much each sale contributes to fixed costs and profit. It is the arithmetic backbone of pricing, mix, and discontinuation decisions: products that look profitable at gross margin can be value-destroyers once variable selling and logistics are loaded. The honest-read risks are allocation of shared variable costs and volume-subsidy illusions, where a high per-unit margin hides a product that cannot cover its capacity footprint. Read with gross margin per product line and product line breakeven coverage.

## Formula

```
Price per Unit - Variable Cost per Unit
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_costing_margin_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1238 (batch 4)
