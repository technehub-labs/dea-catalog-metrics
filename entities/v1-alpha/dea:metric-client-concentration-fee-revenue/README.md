# dea:metric-client-concentration-fee-revenue

Candidate Performance Metric record for **Client Concentration (Fee Revenue)** (CCFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-client-concentration-fee-revenue`
- **Name:** Client Concentration (Fee Revenue)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CCFR

## 2. Definition

A Investment Banking & Capital Markets indicator, Client Concentration (Fee Revenue) (CCFR) quantifies exposure to adverse outcomes. The formula is Largest Client Fees / Total Fees - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Investment banking sector.

## 3. Context

Client concentration in fee revenue measures the share of total fees from the largest clients, and it is the fragility metric of investment banking economics - the fee distribution is extreme (a handful of large corporate and sponsor relationships generate a large share of revenue), which makes the franchise hostage to a few clients' activity levels and to banker departures who take relationships. Concentration dynamics compound: winning a lead-left role on a major client's next deal depends on the last one, so incumbency concentrates further. The honest measurement is at the client group level (sponsors and corporates both), not just mandate level. Read with revenue-at-risk from top-client departures, relationship-coverage breadth (how many bankers touch the account), and the banker-dependency question - concentration in the client plus concentration in the individual is the real risk.

## Formula

```
Largest Client Fees / Total Fees
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
- **Domain:** investment_banking_capital_markets
- **Sector:** investment_banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1149 (batch 4)
