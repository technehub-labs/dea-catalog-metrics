# dea:metric-revenue-growth-rate-deep-dive

Candidate Performance Metric record for **Revenue Growth Rate (Deep Dive)** (RGR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-growth-rate-deep-dive`
- **Name:** Revenue Growth Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RGR-D

## 2. Definition

Revenue Growth Rate (Deep Dive) (RGR-D) addresses growth over time and is a fixture of balanced scorecard - financial perspective reporting. It is computed as (Revenue - Prior Revenue) / Prior Revenue, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures period-over-period expansion of top-line revenue. Growth is the valuation engine, but its quality depends on margin, concentration, and whether it is bought with discounts. Growth measured while excluding churned or divested revenue is a flattering construct. Read with operating margin trend and customer lifetime value trend.

## Formula

```
(Revenue - Prior Revenue) / Prior Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_financial_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3053 (batch 7)
