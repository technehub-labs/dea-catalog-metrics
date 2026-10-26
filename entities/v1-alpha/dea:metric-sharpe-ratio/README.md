# dea:metric-sharpe-ratio

Candidate Performance Metric record for **Sharpe Ratio** (SHARPE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sharpe-ratio`
- **Name:** Sharpe Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SHARPE

## 2. Definition

Sharpe Ratio (SHARPE) measures the economic value created or preserved in the Investment Management domain. It is computed as (Portfolio Return - Risk-Free Rate) / Return Standard Deviation, expressed in ratio (x:1 or x). Its use is concentrated in Asset management. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The Sharpe ratio, introduced by William F. Sharpe (1966), divides excess return over the risk-free rate by the standard deviation of returns - reward per unit of total volatility. A ratio above 1 is decent, above 2 excellent for most strategies; comparing across funds only makes sense within the same asset class and period. Its main caveats: it penalizes upside volatility, it is distorted by non-normal return distributions, and it says nothing about whether risk came from intended factor exposures. Use with Sortino for downside-specific views.

## Formula

```
SHARPE = (Portfolio Return - Risk-Free Rate) / Return Standard Deviation
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management
- **Sector:** asset_management

## Attribution

- **Source credit:** William F. Sharpe, 1966

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 763 (batch 2)
