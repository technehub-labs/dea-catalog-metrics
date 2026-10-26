# dea:metric-beta

Candidate Performance Metric record for **Beta** (BETA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-beta`
- **Name:** Beta
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BETA

## 2. Definition

Beta (BETA) measures exposure to adverse outcomes in the Investment Management domain. It is defined as Covariance of Portfolio and Market Returns / Market Variance; the result is stated in ratio (x:1 or x). In Asset management, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Beta measures a portfolio's sensitivity to market movements - the slope of its regression against benchmark returns - and it is the first risk number every investor learns to read, anchoring CAPM's expected return logic. A beta above 1 amplifies moves; below 1 dampens them. Its trap is instability: beta estimated over five years of history is an average that conceals how the portfolio behaves in stressed regimes, where correlations converge toward 1 and diversifying beta evaporates. Low-beta strategies look seductive in calm markets precisely when they are building crowded positioning. Read with rolling-window beta, downside capture ratio, and factor exposures to understand what is really driving the sensitivity.

## Formula

```
Covariance of Portfolio and Market Returns / Market Variance
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management
- **Sector:** asset_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 766 (batch 2)
