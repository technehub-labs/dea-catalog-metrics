# dea:metric-product-line-breakeven-coverage

Candidate Performance Metric record for **Product Line Breakeven Coverage** (PLBC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-line-breakeven-coverage`
- **Name:** Product Line Breakeven Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PLBC

## 2. Definition

Within Product Costing & Margin Management, Product Line Breakeven Coverage (PLBC) is used to gauge the economic value created or preserved. It is computed as Products above Breakeven Volume / Products Sold, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of a product line's fixed cost base covered by its contribution margin, or how far sales sit above breakeven. It exposes operating leverage risk: two lines with identical margins can carry very different fragility when volumes swing. Its weakness is the fixed-versus-variable split, which is a judgment call and often gamed to make lines look self-funding. Read with contribution margin per unit and capacity utilization to see whether coverage reflects demand or cost-classification choices.

## Formula

```
PLBC = Products above Breakeven Volume / Products Sold
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
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_costing_margin_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1245 (batch 4)
