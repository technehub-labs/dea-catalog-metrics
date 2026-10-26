# dea:metric-leverage-ratio-fund-monitoring

Candidate Performance Metric record for **Leverage Ratio (Fund) Monitoring** (LRFM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-leverage-ratio-fund-monitoring`
- **Name:** Leverage Ratio (Fund) Monitoring
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LRFM

## 2. Definition

Leverage Ratio (Fund) Monitoring (LRFM) measures exposure to adverse outcomes in the Investment Risk & Middle Office Operations domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Gross Exposure / NAV; the result is stated in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. In Investment management, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures whether the fund's leverage is being tracked continuously against regulatory and covenant limits. Leverage converts moderate losses into breaking ones. Monitoring measured at period-end snapshots misses intra-period spikes. Read with stress test scenario coverage and liquidity coverage ratio (Fund Ops).

## Formula

```
Gross Exposure / NAV
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
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3469 (batch 7)
