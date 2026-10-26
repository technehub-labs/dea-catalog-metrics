# dea:metric-share-price-volatility

Candidate Performance Metric record for **Share Price Volatility** (SPV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-share-price-volatility`
- **Name:** Share Price Volatility
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SPV

## 2. Definition

Within Investor Relations & Capital Markets, Share Price Volatility (SPV) is used to gauge exposure to adverse outcomes. Its calculation is Annualized Standard Deviation of Daily Returns, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Listed companies practice.

## 3. Context

The dispersion of the share price over a window, conventionally the annualized standard deviation of returns - the risk metric that prices the company's cost of equity through the beta arithmetic, and the one investors feel directly. Its strategic significance is the feedback loop it participates in: volatility raises the equity discount rate, which lowers valuations, which changes the cost of every equity-funded action the company might take - and high volatility widens the price at which buybacks and issuance transact. The honest read decomposes sources: market-wide volatility, sector volatility, and idiosyncratic moves each have different meanings, and beta-neutral high idiosyncratic volatility usually traces to specific company events or guidance surprises rather than general risk appetite. Read with the liquidity dimension, since thinly traded stocks show mechanical volatility that says nothing about fundamental risk, which is why volatility comparisons need trading-volume context.

## Formula

```
Annualized Standard Deviation of Daily Returns
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investor_relations_capital_markets
- **Sector:** listed_companies

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 629 (batch 2)
