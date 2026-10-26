# dea:metric-asset-allocation-drift-ratio

Candidate Performance Metric record for **Asset Allocation Drift Ratio** (AADR-IM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-allocation-drift-ratio`
- **Name:** Asset Allocation Drift Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AADR-IM

## 2. Definition

Asset Allocation Drift Ratio (AADR-IM) captures conformance to standards, plans, or obligations for organizations tracking investment management - portfolio operations. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Deviation from Target Allocation / Target; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Financial Services, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures how far current portfolio allocation has moved from policy targets. Drift changes the risk profile clients own without their consent and creates rebalancing obligations. Thresholds set too wide make drift chronic by design. Read with rebalancing execution timeliness and mandate compliance breach count.

## Formula

```
Deviation from Target Allocation / Target
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3010 (batch 7)
