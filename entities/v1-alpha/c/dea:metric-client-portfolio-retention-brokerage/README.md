# dea:metric-client-portfolio-retention-brokerage

Candidate Performance Metric record for **Client Portfolio Retention (Brokerage)** (CPBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-client-portfolio-retention-brokerage`
- **Name:** Client Portfolio Retention (Brokerage)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPBR

## 2. Definition

Client Portfolio Retention (Brokerage) (CPBR) addresses the retention of customers, users, or assets over time and is a fixture of insurance distribution & brokerage reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Accounts Retained at Renewal / Accounts at Start; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Insurance distribution, it is a recognized element of the standard performance toolkit.

## 3. Context

Client portfolio retention measures the share of client assets staying put in a brokerage, and it is the compounding metric of the model - brokerage economics work only when assets accumulate, since revenue is basis-point fees on a base that either compounds or erodes. Retention here is asset-based, not just account-based: a client who keeps the account but moves half the assets to a competitor has half-defected, so honest measurement tracks asset outflow net of inflow per relationship. The drivers are differentiated: service quality, performance (real or perceived), and life transitions. Read with net-flow rate by client segment, advisor-transition attrition (assets follow departing advisors), fee-compression-driven outflows to self-directed platforms, and service-failure-triggered withdrawals which are the controllable cause.

## Formula

```
CPBR = Accounts Retained at Renewal / Accounts at Start
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1158 (batch 4)
