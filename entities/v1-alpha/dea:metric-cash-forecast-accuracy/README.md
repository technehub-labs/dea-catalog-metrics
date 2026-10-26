# dea:metric-cash-forecast-accuracy

Candidate Performance Metric record for **Cash Forecast Accuracy** (CFA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-forecast-accuracy`
- **Name:** Cash Forecast Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CFA

## 2. Definition

Cash Forecast Accuracy (CFA) measures the quality of outputs and outcomes in the Treasury & Cash Management domain. Its calculation is 1 - ABS(Actual Cash - Forecast Cash) / Actual Cash, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how close forecasted cash positions land to actuals. It matters because treasury decisions on investment, debt, and hedging all inherit forecast error. Teams can improve it by widening forecast bands or shortening the horizon until misses vanish. Read with Working Capital Ratio trends and Forecast Bias to confirm accuracy gains are structural.

## Formula

```
1 - ABS(Actual Cash - Forecast Cash) / Actual Cash
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 592 (batch 2)
