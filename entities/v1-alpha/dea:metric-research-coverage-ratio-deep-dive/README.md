# dea:metric-research-coverage-ratio-deep-dive

Candidate Performance Metric record for **Research Coverage Ratio (Deep Dive)** (RCR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-research-coverage-ratio-deep-dive`
- **Name:** Research Coverage Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCR-D

## 2. Definition

Research Coverage Ratio (Deep Dive) (RCR-D) addresses capability maturity or development and is a fixture of investment research & trading operations reporting. Its calculation is Covered Names / Portfolio Holdings, measured in percent (%). It originates from and is most used in Financial Services practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of portfolio holdings or target universe covered by active analyst research. Coverage is the information edge underpinning conviction: uncovered holdings are essentially passive bets at active prices. Coverage counted by name rather than by position weight can hide the largest exposures. Read with analyst recommendation hit rate and active share.

## Formula

```
RCR-D = Covered Names / Portfolio Holdings
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3029 (batch 7)
