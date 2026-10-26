# dea:metric-subscription-retention-rate-publishing

Candidate Performance Metric record for **Subscription Retention Rate (Publishing)** (SRR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-subscription-retention-rate-publishing`
- **Name:** Subscription Retention Rate (Publishing)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SRR-P

## 2. Definition

Subscription Retention Rate (Publishing) (SRR-P) captures the retention of customers, users, or assets over time for organizations tracking printing & publishing. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Subscriptions Renewed / Subscriptions Expiring, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Printing & publishing practice.

## 3. Context

Measures the share of subscribers renewing over a period, the core engine of publishing economics as recurring digital subscriptions replace newsstand and advertising volatility. It matters because a few points of retention compound dramatically over acquisition spend payback. Honest reads separate price-driven cancels from engagement-driven ones, and watch for inactive zombie subscriptions that inflate the rate until payment failures sweep them out. Read with subscriber churn reasons, engagement frequency, and ARPU trend.

## Formula

```
Subscriptions Renewed / Subscriptions Expiring
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** printing_publishing
- **Sector:** printing_publishing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1265 (batch 4)
