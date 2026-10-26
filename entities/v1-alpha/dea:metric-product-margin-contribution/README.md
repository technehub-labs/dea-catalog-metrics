# dea:metric-product-margin-contribution

Candidate Performance Metric record for **Product Margin Contribution** (PMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-margin-contribution`
- **Name:** Product Margin Contribution
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PMC

## 2. Definition

Within Product Management, Product Margin Contribution (PMC) is used to gauge the economic value created or preserved. Its calculation is (Product Revenue - Product Cost) / Product Revenue, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of total margin contributed by a product or line - the profitability-decomposition metric that corrects revenue's most misleading habit: revenue-share tables reward high-volume, low-margin products that consume the organization's attention and capacity while returning little. Its strategic significance is portfolio truth: the classic product-portfolio finding is that margin concentrates, and the contribution view surfaces the few products carrying the many - which is where investment, roadmap priority, and pricing protection belong. The allocation honesty determines credibility: shared costs allocated by revenue (rather than by driver) systematically flatter the biggest products and hide the small high-margin ones, so activity-based or at least driver-based allocation is the price of a trustworthy number. Read with the trend: contribution share drifting from a product whose revenue holds steady indicates margin erosion under competitive pressure, which revenue-share metrics never show.

## Formula

```
(Product Revenue - Product Cost) / Product Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 559 (batch 1)
