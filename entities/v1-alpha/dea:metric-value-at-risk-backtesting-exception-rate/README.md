# dea:metric-value-at-risk-backtesting-exception-rate

Candidate Performance Metric record for **Value at Risk Backtesting Exception Rate** (VARBER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-value-at-risk-backtesting-exception-rate`
- **Name:** Value at Risk Backtesting Exception Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** VARBER

## 2. Definition

Value at Risk Backtesting Exception Rate (VARBER) measures exposure to adverse outcomes in the Investment Risk & Middle Office Operations domain. The formula is Exceptions beyond VaR Model Tolerance / Backtest Days - reported in percent (%). It is a standard measure in the Investment management sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how often actual losses exceed the model's VaR predictions. Backtesting is the falsifiable test of a risk model: too many exceptions means a broken model, too few means excessive conservatism. Exception counting during regime changes punishes models for history. Read with expected shortfall estimate stability and model validation currency (Investment).

## Formula

```
Exceptions beyond VaR Model Tolerance / Backtest Days
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3457 (batch 7)
