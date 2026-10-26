# dea:metric-return-rate

Candidate Performance Metric record for **Return Rate** (RTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-rate`
- **Name:** Return Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RTR

## 2. Definition

Return Rate (RTR) captures exposure to adverse outcomes for organizations tracking retail & e-commerce. It is defined as Returned Orders / Orders Shipped; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. In Retail, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of sold items returned by customers. It matters because returns reverse revenue and consume logistics and processing cost. Gaming risk includes tightening return windows or classifying returns as exchanges to shrink the measured rate. Read with Net Revenue and Product Quality complaint trends to confirm a falling return rate means happier customers, not deterred ones.

## Formula

```
Returned Orders / Orders Shipped
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 498 (batch 1)
