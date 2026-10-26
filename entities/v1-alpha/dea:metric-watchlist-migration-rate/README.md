# dea:metric-watchlist-migration-rate

Candidate Performance Metric record for **Watchlist Migration Rate** (WMR-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-watchlist-migration-rate`
- **Name:** Watchlist Migration Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WMR-CC

## 2. Definition

A Credit & Collections Risk (Enterprise) indicator, Watchlist Migration Rate (WMR-CC) quantifies exposure to adverse outcomes. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Accounts Migrating to Watchlist / Monitored Accounts, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
WMR-CC = Accounts Migrating to Watchlist / Monitored Accounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4211 (batch 9)
