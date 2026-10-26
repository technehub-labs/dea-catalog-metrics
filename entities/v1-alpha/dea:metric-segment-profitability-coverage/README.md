# dea:metric-segment-profitability-coverage

Candidate Performance Metric record for **Segment Profitability Coverage** (SPC-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-segment-profitability-coverage`
- **Name:** Segment Profitability Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SPC-A

## 2. Definition

A Customer Analytics & Insights indicator, Segment Profitability Coverage (SPC-A) quantifies capability maturity or development. The formula is Segments with Current Profitability Model / Active Segments - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of customer segments with verified profitability data. It matters because profit-blind targeting optimizes revenue while destroying margin. Coverage can be met with fully allocated guesses rather than measured economics. Read with Activity-Based Costing Coverage and segment margin variance to confirm profitability numbers are defensible.

## Formula

```
Segments with Current Profitability Model / Active Segments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** customer_analytics_insights

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1427 (batch 5)
