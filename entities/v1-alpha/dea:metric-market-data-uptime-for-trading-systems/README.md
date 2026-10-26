# dea:metric-market-data-uptime-for-trading-systems

Candidate Performance Metric record for **Market Data Uptime for Trading Systems** (MDUT-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-market-data-uptime-for-trading-systems`
- **Name:** Market Data Uptime for Trading Systems
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MDUT-T

## 2. Definition

Market Data Uptime for Trading Systems (MDUT-T) measures the utilization or availability of capacity in the Investment Research & Trading Operations domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Feed Available Time / Required Time; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Financial Services, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures availability of critical market data feeds during trading hours. Data gaps blind trading and risk systems at precisely the moments that matter most. Uptime measured on feed receipt rather than on staleness/latency thresholds can look perfect while serving stale prices. Read with latency percentile compliance and incident volume for trading systems.

## Formula

```
Feed Available Time / Required Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3048 (batch 7)
