# dea:metric-portfolio-turnover-ratio

Candidate Performance Metric record for **Portfolio Turnover Ratio** (PTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-turnover-ratio`
- **Name:** Portfolio Turnover Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PTR

## 2. Definition

A Investment Management indicator, Portfolio Turnover Ratio (PTR) quantifies how efficiently resources are converted into outputs. It is defined as Min(Purchases, Sales) / Average Portfolio Value; the result is stated in ratio (x:1 or x). In Asset management, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Portfolio turnover measures the share of a portfolio's holdings traded in a period, and it is a two-edged metric: high turnover signals active conviction and adaptiveness but also generates transaction costs, short-term capital gains distributions (painful for taxable investors), and potential tax inefficiency. Low turnover in an active fund can signal either disciplined buy-and-hold conviction or a manager who has stopped doing the work. Turnover's real cost depends on implementation: the same turnover rate in small-cap emerging markets stocks costs far more in market impact than in large-cap US equities. Read with expense drag from trading costs and tax-loss harvesting efficiency.

## Formula

```
PTR = Min(Purchases, Sales) / Average Portfolio Value
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 771 (batch 2)
