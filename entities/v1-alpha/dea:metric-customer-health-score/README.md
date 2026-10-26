# dea:metric-customer-health-score

Candidate Performance Metric record for **Customer Health Score** (CHS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-health-score`
- **Name:** Customer Health Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CHS

## 2. Definition

A Customer indicator, Customer Health Score (CHS) quantifies exposure to adverse outcomes. It is defined as Weighted Index of Usage, Satisfaction, and Support Signals; the result is stated in index (0-100 or normalized). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures a composite index of usage, engagement, support signals, and relationship factors predicting account risk. It matters because it converts scattered signals into an early-warning system for churn and expansion. The weighting model can be tuned retrospectively until it looks predictive, hiding weak real-world signal. Read with Net Revenue Retention and Churn Rate to validate whether health scores actually anticipate outcomes.

## Formula

```
Weighted Index of Usage, Satisfaction, and Support Signals
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 77 (batch 1)
