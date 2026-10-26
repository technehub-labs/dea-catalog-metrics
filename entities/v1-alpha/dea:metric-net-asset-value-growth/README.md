# dea:metric-net-asset-value-growth

Candidate Performance Metric record for **Net Asset Value Growth** (NAVG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-asset-value-growth`
- **Name:** Net Asset Value Growth
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NAVG

## 2. Definition

A Investment Management indicator, Net Asset Value Growth (NAVG) quantifies growth over time. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is (NAV_current - NAV_prior) / NAV_prior, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Asset management practice.

## 3. Context

Net asset value growth tracks the increase in a fund's per-share value, and it is the headline number in most fund marketing - the metric investors quote to each other and the basis for league tables. But total-return NAV growth conflates three distinct things: underlying asset appreciation, income distribution reinvestment, and flows-driven effects, so the honest read requires separating price return from total return and checking whether growth came from market beta or manager skill. For closed-end funds and interval funds, NAV growth can diverge from share price, creating premium/discount dynamics. Read with alpha, benchmark-relative growth, and flow-adjusted returns.

## Formula

```
(NAV_current - NAV_prior) / NAV_prior
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 769 (batch 2)
