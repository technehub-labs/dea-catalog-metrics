# dea:metric-budget-forecast-accuracy-financial-planning-deep-dive

Candidate Performance Metric record for **Budget Forecast Accuracy - Financial Planning (Deep Dive)** (BFAD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-budget-forecast-accuracy-financial-planning-deep-dive`
- **Name:** Budget Forecast Accuracy - Financial Planning (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BFAD

## 2. Definition

Within Balanced Scorecard - Financial Perspective, Budget Forecast Accuracy - Financial Planning (Deep Dive) (BFAD) is used to gauge the quality of outputs and outcomes. Its calculation is 1 - Absolute Forecast Error / Actual, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how closely actual financial results track the plan. Forecast accuracy determines the credibility of every guidance commitment downstream. Accuracy from sandbagged forecasts is a different dysfunction from skill. Read with estimate accuracy - cost and management information freshness score.

## Formula

```
BFAD = 1 - Absolute Forecast Error / Actual
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3065 (batch 7)
