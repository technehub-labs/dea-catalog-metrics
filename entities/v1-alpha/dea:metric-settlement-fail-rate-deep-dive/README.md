# dea:metric-settlement-fail-rate-deep-dive

Candidate Performance Metric record for **Settlement Fail Rate (Deep Dive)** (SEFR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-settlement-fail-rate-deep-dive`
- **Name:** Settlement Fail Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SEFR-D

## 2. Definition

Settlement Fail Rate (Deep Dive) (SEFR-D) addresses exposure to adverse outcomes and is a fixture of investment management - portfolio operations reporting. It is a working-level control: thresholds trigger immediate operational response. It is defined as Failed Settlements / Settlements; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Financial Services, it is a recognized element of the standard performance toolkit.

## Formula

```
SEFR-D = Failed Settlements / Settlements
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3015 (batch 7)
