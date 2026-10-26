# dea:metric-compound-annual-growth-rate-deep-dive

Candidate Performance Metric record for **Compound Annual Growth Rate (Deep Dive)** (CAGRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compound-annual-growth-rate-deep-dive`
- **Name:** Compound Annual Growth Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAGRDD

## 2. Definition

Compound Annual Growth Rate (Deep Dive) (CAGRDD) captures growth over time for organizations tracking market structure & economics standard measures. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as (Ending Value / Beginning Value)^(1/Years) - 1, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the annualized growth rate over a multi-year period. CAGR smooths volatility into a comparable trend number. Endpoint choice can manufacture the story: start low, end high. Read with revenue growth rate (Deep Dive) and market growth capture ratio.

## Formula

```
CAGRDD = (Ending Value / Beginning Value)^(1/Years) - 1
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** growth
- **Scope classification:** business_domain
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** market_structure_economics_standard_measures

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4138 (batch 9)
