# dea:metric-renewal-retention-ratio-underwriting

Candidate Performance Metric record for **Renewal Retention Ratio (Underwriting)** (RRR-U) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-renewal-retention-ratio-underwriting`
- **Name:** Renewal Retention Ratio (Underwriting)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRR-U

## 2. Definition

Renewal Retention Ratio (Underwriting) (RRR-U) addresses the retention of customers, users, or assets over time and is a fixture of insurance underwriting reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Policies Renewed / Policies Eligible for Renewal; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Insurance, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of in-force premium renewing, weighted by premium, at policy term. It is the retention backbone of insurance economics, since profitable books compound through renewal while acquisition costs amortize over the life. Be alert to retention bought with below-technical renewals, and to policy-count retention masking premium erosion. Read with rate change at renewal and underwriting loss ratio for retained business quality.

## Formula

```
RRR-U = Policies Renewed / Policies Eligible for Renewal
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1516 (batch 6)
