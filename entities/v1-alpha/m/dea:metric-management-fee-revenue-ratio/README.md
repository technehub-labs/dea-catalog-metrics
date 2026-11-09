# dea:metric-management-fee-revenue-ratio

Candidate Performance Metric record for **Management Fee Revenue Ratio** (MFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-management-fee-revenue-ratio`
- **Name:** Management Fee Revenue Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MFR

## 2. Definition

Within Investment Management, Management Fee Revenue Ratio (MFR) is used to gauge the economic value created or preserved. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Management Fees / Average Assets under Management; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Asset management, it is a recognized element of the standard performance toolkit.

## 3. Context

Management fee revenue ratio measures fee income as a share of assets under management, and it is the effective realization rate of the manager's business model - a blend of contracted fee schedules, client mix (institutional fees are lower than retail), and negotiated breakpoints. A declining ratio signals fee compression, the industry-wide pressure that has pushed average asset-fee rates down for a decade, and it directly hits profitability since management fees are the high-margin revenue core. The strategic question is mix: is ratio decline coming from institutionalization of the client base (possibly healthy for asset stickiness) or from competitive discounting? Read with net revenue margin and client-mix trends.

## Formula

```
MFR = Management Fees / Average Assets under Management
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management
- **Sector:** asset_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 770 (batch 2)
