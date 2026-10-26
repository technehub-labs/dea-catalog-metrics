# dea:metric-promotion-forecast-accuracy

Candidate Performance Metric record for **Promotion Forecast Accuracy** (PFA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-promotion-forecast-accuracy`
- **Name:** Promotion Forecast Accuracy
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PFA

## 2. Definition

Promotion Forecast Accuracy (PFA) addresses the quality of outputs and outcomes and is a fixture of sales & operations planning reporting. Its calculation is 1 - ABS(Promotional Forecast - Actual) / Actual, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how accurately promotion demand uplift is forecast. It matters because promotion misses create both stockouts and excess that destroy promo economics. Forecasters can improve accuracy by always forecasting zero uplift, minimizing error on frequent small promos. Read with Promotion ROI and Post-Promo Inventory to confirm accuracy holds where it is hard.

## Formula

```
1 - ABS(Promotional Forecast - Actual) / Actual
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1295 (batch 5)
