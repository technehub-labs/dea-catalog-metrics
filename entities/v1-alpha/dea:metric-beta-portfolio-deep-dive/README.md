# dea:metric-beta-portfolio-deep-dive

Candidate Performance Metric record for **Beta (Portfolio) (Deep Dive)** (BTPDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-beta-portfolio-deep-dive`
- **Name:** Beta (Portfolio) (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BTPDD

## 2. Definition

Beta (Portfolio) (Deep Dive) (BTPDD) measures exposure to adverse outcomes in the Investment Performance Measurement domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Covariance with Market / Market Variance, expressed in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Its use is concentrated in Investment management.

## 3. Context

Portfolio beta, from the CAPM tradition (Sharpe, Treynor, Lintner), is the covariance of portfolio and market returns divided by market variance - the sensitivity of the portfolio to market moves. Beta 1 moves with the market, 2 doubles the ride, 0.5 halves it. Its practical failings: beta is estimated with error and drifts with the estimation window, it captures co-movement not exposure (a crash-tested portfolio can carry a deceptively low beta in calm times), and it assumes the relationship is linear. Use it for asset-allocation conversations, not for risk measurement of tail events.

## Formula

```
Covariance with Market / Market Variance
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Capital Asset Pricing Model (Sharpe, Treynor, Lintner)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3440 (batch 7)
