# dea:metric-season-ticket-renewal-rate

Candidate Performance Metric record for **Season Ticket Renewal Rate** (STRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-season-ticket-renewal-rate`
- **Name:** Season Ticket Renewal Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** STRR

## 2. Definition

Season Ticket Renewal Rate (STRR) measures the retention of customers, users, or assets over time in the Sports & Events domain. The formula is Season Tickets Renewed / Season Tickets Expiring - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Sports & events sector.

## 3. Context

Season ticket renewal rate measures the share of season-ticket holders retaining year over year, and it is the revenue foundation of sports franchises - season tickets are the annuity base that guarantees revenue before a single game and funds long-term stadium commitments. The metric is deceptive in its simplicity because season-ticket retention is affected by performance (bad seasons suppress renewal), pricing (aggressive annual increases test loyalty), and experience (seat neighbors, service quality). Renewal timing matters: early-bird windows with incentives raise rates and cash-flow timing simultaneously. The renewal-plus-waitlist composite is the true health measure - a team with high renewal but a thin waitlist has pricing power but no growth pipeline. Read with waitlist depth, renewal by tenure cohort (long-tenure fans renew differently), price-increase elasticity, and win-percentage correlation with a lag.

## Formula

```
Season Tickets Renewed / Season Tickets Expiring
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** sports_events
- **Sector:** sports_events

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 948 (batch 3)
