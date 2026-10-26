# dea:metric-churn-prediction-coverage

Candidate Performance Metric record for **Churn Prediction Coverage** (CPC-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-churn-prediction-coverage`
- **Name:** Churn Prediction Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPC-S

## 2. Definition

Churn Prediction Coverage (CPC-S) addresses exposure to adverse outcomes and is a fixture of customer success (b2b saas) reporting. Its calculation is At-Risk Accounts with Active Save Plan / At-Risk Accounts, measured in percent (%). It originates from and is most used in Software & SaaS practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of the customer base scored by churn prediction models. It matters because unmonitored accounts churn invisibly. Coverage can be 100 percent while accuracy is near zero, so coverage alone proves little. Read with Churn Model Accuracy and proactive-save win rates to confirm coverage converts into retained revenue.

## Formula

```
At-Risk Accounts with Active Save Plan / At-Risk Accounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 585 (batch 2)
