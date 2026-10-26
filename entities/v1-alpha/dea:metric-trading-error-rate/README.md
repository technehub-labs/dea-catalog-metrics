# dea:metric-trading-error-rate

Candidate Performance Metric record for **Trading Error Rate** (TER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trading-error-rate`
- **Name:** Trading Error Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TER

## 2. Definition

Trading Error Rate (TER) addresses exposure to adverse outcomes and is a fixture of investment banking & capital markets reporting. The formula is Erroneous Trades / Total Trades - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Investment banking sector.

## Formula

```
Erroneous Trades / Total Trades
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_banking_capital_markets
- **Sector:** investment_banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1151 (batch 4)
