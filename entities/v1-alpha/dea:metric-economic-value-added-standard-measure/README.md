# dea:metric-economic-value-added-standard-measure

Candidate Performance Metric record for **Economic Value Added (Standard Measure)** (EVA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-economic-value-added-standard-measure`
- **Name:** Economic Value Added (Standard Measure)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EVA

## 2. Definition

Economic Value Added (Standard Measure) (EVA) captures the economic value created or preserved for organizations tracking valuation & corporate finance standard measures. It is defined as NOPAT - (Invested Capital x WACC); the result is stated in currency value. It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures operating profit less the full charge for capital employed. EVA converts performance to the only question that matters: was value created above the cost of capital? Positive EVA on a declining trend signals regression toward the hurdle. Read with ROIC-WACC spread and economic value added (Deep Dive).

## Formula

```
NOPAT - (Invested Capital x WACC)
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** valuation_corporate_finance_standard_measures

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4039 (batch 9)
