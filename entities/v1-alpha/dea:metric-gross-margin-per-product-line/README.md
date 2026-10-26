# dea:metric-gross-margin-per-product-line

Candidate Performance Metric record for **Gross Margin per Product Line** (GMPL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-margin-per-product-line`
- **Name:** Gross Margin per Product Line
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GMPL

## 2. Definition

Gross Margin per Product Line (GMPL) addresses the economic value created or preserved and is a fixture of product costing & margin management reporting. It is computed as (Product Revenue - Cost of Sales) / Product Revenue, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Aggregates revenue less cost of goods sold at the product-line level, revealing where the portfolio actually earns its margin rather than where headline revenue grows. It anchors portfolio strategy because many firms chase revenue lines that dilute blended margin. Watch for channel and mix shifts masquerading as price performance, and for cost accounting conventions (standard cost updates, inventory valuation) that can swing the number without any real change. Read with contribution margin per unit and product line breakeven coverage.

## Formula

```
(Product Revenue - Cost of Sales) / Product Revenue
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1239 (batch 4)
