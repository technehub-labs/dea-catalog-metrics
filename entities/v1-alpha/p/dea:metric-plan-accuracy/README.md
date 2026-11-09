# dea:metric-plan-accuracy

Candidate Performance Metric record for **Plan Accuracy** (PLAN) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-plan-accuracy`
- **Name:** Plan Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PLAN

## 2. Definition

A Operations indicator, Plan Accuracy (PLAN) quantifies the quality of outputs and outcomes. It is defined as 1 - ABS(Actual - Plan) / Plan; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how closely actual production or demand outcomes match the plan. It matters because planning error cascades into inventory, overtime, and service failures. Teams can improve it by planning trivially conservative volumes that guarantee small misses. Read with Forecast Bias and Production Plan Attainment to separate genuine forecasting skill from sandbagged plans.

## Formula

```
PLAN = 1 - ABS(Actual - Plan) / Plan
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
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 173 (batch 1)
