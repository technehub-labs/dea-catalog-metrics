# dea:metric-demand-forecast-accuracy-workforce

Candidate Performance Metric record for **Demand Forecast Accuracy (Workforce)** (DFAW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-demand-forecast-accuracy-workforce`
- **Name:** Demand Forecast Accuracy (Workforce)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DFAW

## 2. Definition

Within Workforce Planning & Analytics, Demand Forecast Accuracy (Workforce) (DFAW) is used to gauge the quality of outputs and outcomes. It is defined as 1 - ABS(Forecast Staffing - Required Staffing) / Required Staffing; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how accurately workforce demand is forecast for staffing plans. It matters because labor plans inherit forecast error as overtime or idle cost. Accuracy can be inflated by forecasting trivially stable demand. Read with Labor Cost Variance and Schedule Adherence to confirm accuracy converts into staffing efficiency.

## Formula

```
1 - ABS(Forecast Staffing - Required Staffing) / Required Staffing
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1450 (batch 5)
