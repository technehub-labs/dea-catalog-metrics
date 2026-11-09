# dea:metric-revenue-leakage-rate

Candidate Performance Metric record for **Revenue Leakage Rate** (RVL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-leakage-rate`
- **Name:** Revenue Leakage Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RVL

## 2. Definition

Revenue Leakage Rate (RVL) measures exposure to adverse outcomes in the Pricing & Revenue Management domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Detected Under-Billing and Missed Billing / Total Revenue; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Revenue leakage rate measures revenue lost to billing errors, un-billed services, contract non-compliance, and missed charges - the gap between what was earned and what was invoiced - and it is the silent-erosion metric of revenue operations. Its sources are structural rather than malicious: contract terms not translated into billing systems, usage not metered correctly, renewals missed, service credits not captured. The distinctive danger of leakage is its invisibility - customers rarely complain about under-billing, so leakage persists for years without surfacing. The measurement approach is audit-based, which makes it sampling-sensitive and dependent on audit scope honesty. Read with leakage-recovery rate (identified leakage collected is real money; identified but written off is a governance signal), leakage-by-cause distribution, and recurrence analysis (leakage that recurs in the same source signals process failure, not error).

## Formula

```
RVL = Detected Under-Billing and Missed Billing / Total Revenue
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1073 (batch 4)
