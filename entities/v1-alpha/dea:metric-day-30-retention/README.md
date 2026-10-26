# dea:metric-day-30-retention

Candidate Performance Metric record for **Day 30 Retention** (D30R) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-day-30-retention`
- **Name:** Day 30 Retention
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** D30R

## 2. Definition

A Gaming indicator, Day 30 Retention (D30R) quantifies the retention of customers, users, or assets over time. The formula is Players Returning on Day 30 / New Player Cohort - reported in percent (%). It is a standard measure in the Gaming sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of a cohort still active after a month - the mature-checkpoint retention metric of gaming, and the one that separates live-service products from launch products: a game holding a meaningful share of its cohort at day 30 has become a habit with content depth, and that is the population that sustains the game's economy. Its strategic significance is the LTV anchor: lifetime value models weight day-30 behavior heavily because early spend without retention is monetization without a business, and user-acquisition bidding becomes sustainable only when day-30 retention supports the projected lifetime revenue. The honest read is curve-shape: the decay between day 7 and day 30 matters more than the endpoint - a curve flattening at day 14 indicates a stable niche population, while continued steep decay indicates the content cadence never engaged - and the remedies differ. Read with the progression dimension: players at endgame versus mid-progression at day 30 reveal whether the game kept them or the social graph did.

## Formula

```
Players Returning on Day 30 / New Player Cohort
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
- **Domain:** gaming
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 709 (batch 2)
