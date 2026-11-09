# dea:metric-deposit-growth-rate

Candidate Performance Metric record for **Deposit Growth Rate** (DGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deposit-growth-rate`
- **Name:** Deposit Growth Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DGR

## 2. Definition

Within Banking & Financial Services, Deposit Growth Rate (DGR) is used to gauge growth over time. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is (Deposits_current - Deposits_prior) / Deposits_prior - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Financial services sector.

## 3. Context

Period-over-period growth in customer deposits - the funding-side growth metric for deposit-taking institutions. Deposits are structurally the cheapest and stickiest funding a bank can have, so the rate measures whether the franchise is compounding its funding advantage or being forced toward wholesale markets. The strategic questions are mix and price: growth bought with promotional rates is just wholesale funding in disguise, while growth in low-cost current accounts is genuine franchise value. It is also a denominator for system-level concerns - in fast-growing emerging markets, deposit growth far above loan growth signals deepening; the reverse signals that credit is being funded from sources that can leave quickly.

## Formula

```
DGR = (Deposits_current - Deposits_prior) / Deposits_prior
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 45 (batch 1)
