# dea:metric-day-7-retention

Candidate Performance Metric record for **Day 7 Retention** (D7R) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-day-7-retention`
- **Name:** Day 7 Retention
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** D7R

## 2. Definition

Day 7 Retention (D7R) measures the retention of customers, users, or assets over time in the Gaming domain. Its calculation is Players Returning on Day 7 / New Player Cohort, measured in percent (%). It originates from and is most used in Gaming practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of a cohort active on day seven - the second checkpoint, and the one that measures whether the game found its place in the player's routine: day 1 asks whether the first session worked, day 7 asks whether the experience compounds - whether progression, social connection, or content cadence gave a reason to keep returning through the week. Its strategic significance is the monetization gate: industry experience is that payers concentrate among players who survive the first week, so day-7 retention is the leading indicator of payer conversion and LTV, and it is the checkpoint against which user-acquisition payback math is validated. The honest read pairs with day 1: high day-1 with weak day-7 decay indicates a strong first impression with weak depth - the content-or-progression problem - while low day-1 with a flat curve indicates the survivors are committed, an audience-fit question. The week-by-week curve between the two checkpoints is where the decay shape and its diagnosis live.

## Formula

```
D7R = Players Returning on Day 7 / New Player Cohort
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 708 (batch 2)
