# dea:metric-realization-slippage-rate

Candidate Performance Metric record for **Realization Slippage Rate** (RSR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-realization-slippage-rate`
- **Name:** Realization Slippage Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RSR-P

## 2. Definition

Within PMO & Portfolio Governance, Realization Slippage Rate (RSR-P) is used to gauge the economic value created or preserved. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Benefits Realized Later than Plan / Planned Benefits - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how far actual benefit realization lags the business case timeline. Slippage is the compound interest of overpromised cases. Slippage attributed to 'adoption delays' often reflects benefits that were never real. Read with benefits realization rate and business case quality score.

## Formula

```
Benefits Realized Later than Plan / Planned Benefits
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pmo_portfolio_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3416 (batch 7)
