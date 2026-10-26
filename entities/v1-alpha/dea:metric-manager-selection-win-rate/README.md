# dea:metric-manager-selection-win-rate

Candidate Performance Metric record for **Manager Selection Win Rate** (MSWR-IM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-manager-selection-win-rate`
- **Name:** Manager Selection Win Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MSWR-IM

## 2. Definition

Within Investment Management - Portfolio Operations, Manager Selection Win Rate (MSWR-IM) is used to gauge how effectively a process or entity achieves its intended outcome. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Selected Managers Outperforming over Period / Selected - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Financial Services sector.

## 3. Context

Measures the share of selected managers that outperform their benchmark or peers over the evaluation horizon. Selection skill is the core value proposition of multi-manager platforms. Short-horizon win rates are statistically indistinguishable from luck. Read with excess return over benchmark and manager tenure.

## Formula

```
Selected Managers Outperforming over Period / Selected
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3009 (batch 7)
