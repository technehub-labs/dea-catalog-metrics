# dea:metric-average-revenue-per-paying-user

Candidate Performance Metric record for **Average Revenue per Paying User** (ARPPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-revenue-per-paying-user`
- **Name:** Average Revenue per Paying User
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ARPPU

## 2. Definition

Within Gaming, Average Revenue per Paying User (ARPPU) is used to gauge the economic value created or preserved. The formula is Revenue / Paying Users - reported in currency per unit. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Gaming sector.

## 3. Context

Revenue divided by paying users in the period - the spending-depth metric of gaming monetization, and the one that isolates what the players who actually pay are spending. Its strategic significance is the concentration lens: free-to-play economies historically monetize a small share of players deeply, and ARPPU tracks that depth - so the pairing of ARPPU with payer conversion is the entire monetization story, and improving one often moves the other in the opposite direction. The strategic tension is design philosophy: raising ARPPU through aggressive monetization mechanics (gacha depth, pay-to-win pressure) raises short-term revenue and can churn the non-paying base that provides the multiplayer vitality - the ecosystem argument that is the industry's central design debate. Read with spend-distribution shape: average ARPPU on heavily skewed spend distributions is dominated by top spenders, so median and top-decile splits are the honest companion before any monetization change is judged.

## Formula

```
ARPPU = Revenue / Paying Users
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 704 (batch 2)
