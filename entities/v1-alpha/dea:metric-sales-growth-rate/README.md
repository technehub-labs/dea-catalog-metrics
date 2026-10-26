# dea:metric-sales-growth-rate

Candidate Performance Metric record for **Sales Growth Rate** (SGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sales-growth-rate`
- **Name:** Sales Growth Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SGR

## 2. Definition

A Sales indicator, Sales Growth Rate (SGR) quantifies growth over time. Its calculation is (Sales_current - Sales_prior) / Sales_prior, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Period-over-period growth in sales - the topline heartbeat of the commercial organization, and the first number in every operating review because it carries the momentum narrative that valuation multiples extend. The strategic value is decomposition: growth split by region, product, and existing versus new business reveals whether expansion is broad-based or a single hot segment masking stagnation elsewhere. Unlike revenue growth in the financial sense, this is an operating metric owned by sales leadership, which makes it gameable - pull-forward deals, quarter-end discounting, and channel stuffing all manufacture the rate for one period at the cost of the next. Read it with pipeline coverage and win-rate trends to separate durable growth from bought growth.

## Formula

```
(Sales_current - Sales_prior) / Sales_prior
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 86 (batch 1)
