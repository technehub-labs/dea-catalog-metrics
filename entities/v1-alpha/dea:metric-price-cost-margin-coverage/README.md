# dea:metric-price-cost-margin-coverage

Candidate Performance Metric record for **Price Cost Margin Coverage** (PCMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-price-cost-margin-coverage`
- **Name:** Price Cost Margin Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PCMC

## 2. Definition

Price Cost Margin Coverage (PCMC) addresses the economic value created or preserved and is a fixture of pricing & revenue management reporting. It is computed as (Price - Variable Cost) / Price, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Price cost margin coverage measures whether realized prices exceed the fully loaded cost of the product or service - the margin floor test - and it is the pricing-discipline metric that catches the quiet killer of many businesses: volume growth at prices that do not cover incremental cost. The metric's strategic content is the contribution-margin decision: not every sale should be made, and the discipline of walking away from below-cost business is what separates healthy pricing organizations from desperate ones. The measurement complexity is cost allocation: fully loaded versus incremental cost produce different verdicts on the same deal (a price above incremental but below fully loaded cost may still be right if capacity is idle). Read with customer-profitability distribution (the aggregate version), discount approval against margin thresholds, and product-line margin trends.

## Formula

```
PCMC = (Price - Variable Cost) / Price
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1070 (batch 4)
