# dea:metric-fee-realization-rate-wealth-deep-dive

Candidate Performance Metric record for **Fee Realization Rate (Wealth Deep Dive)** (FRR-W) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fee-realization-rate-wealth-deep-dive`
- **Name:** Fee Realization Rate (Wealth Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FRR-W

## 2. Definition

Fee Realization Rate (Wealth Deep Dive) (FRR-W) addresses the economic value created or preserved and is a fixture of asset & wealth management (deep dive) reporting. It is defined as Fees Collected / Fees Billable; the result is stated in percent (%). In Financial Services, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures fees actually collected against contractual fee schedules. Realization gaps arise from breakpoints, negotiated concessions, fee waivers, and billing errors, and in wealth management they are a silent margin leak measured in percentage points of revenue. Systematic billing-audit evidence is the only defensible basis for the rate, since manual billing accumulates errors. Read with discount-approval compliance and billing exception aging.

## Formula

```
Fees Collected / Fees Billable
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
- **Domain:** asset_wealth_management_deep_dive
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2113 (batch 6)
