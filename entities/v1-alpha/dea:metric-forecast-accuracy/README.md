# dea:metric-forecast-accuracy

Candidate Performance Metric record for **Forecast Accuracy** (FA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-forecast-accuracy`
- **Name:** Forecast Accuracy
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FA

## 2. Definition

Within Sales, Forecast Accuracy (FA) is used to gauge the quality of outputs and outcomes. It is computed as 1 - ABS(Actual - Forecast) / Actual, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how close the sales forecast lands to actual bookings. It matters because supply, hiring, and investor guidance all hinge on it. Gaming risk includes forecasting conservatively to guarantee beats, or sandbagging then quietly closing the gap with pulled-forward deals. Read with Bookings to Target and Opportunity Slippage Rate to distinguish forecasting skill from managed expectations.

## Formula

```
1 - ABS(Actual - Forecast) / Actual
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 93 (batch 1)
