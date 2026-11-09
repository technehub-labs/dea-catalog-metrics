# dea:metric-overlimit-rate

Candidate Performance Metric record for **Overlimit Rate** (OLR-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overlimit-rate`
- **Name:** Overlimit Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OLR-CC

## 2. Definition

Within Credit & Collections Risk (Enterprise), Overlimit Rate (OLR-CC) is used to gauge exposure to adverse outcomes. Its calculation is Accounts above Approved Limit / Accounts, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
OLR-CC = Accounts above Approved Limit / Accounts
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4207 (batch 9)
