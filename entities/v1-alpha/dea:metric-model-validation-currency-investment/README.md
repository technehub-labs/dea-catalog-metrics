# dea:metric-model-validation-currency-investment

Candidate Performance Metric record for **Model Validation Currency (Investment)** (MVCI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-validation-currency-investment`
- **Name:** Model Validation Currency (Investment)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MVCI

## 2. Definition

Model Validation Currency (Investment) (MVCI) addresses conformance to standards, plans, or obligations and is a fixture of investment risk & middle office operations reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Pricing and Risk Models Validated within Cycle / Due, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Investment management practice.

## 3. Context

Measures whether risk and pricing models have been validated within their required cycles. Unvalidated models produce numbers with unwarranted authority. Validation currency measured as document date rather than substance is stale assurance. Read with model validation backlog and value at risk backtesting exception rate.

## Formula

```
MVCI = Pricing and Risk Models Validated within Cycle / Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3473 (batch 7)
