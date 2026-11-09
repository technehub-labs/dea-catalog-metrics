# dea:metric-day-1-retention

Candidate Performance Metric record for **Day 1 Retention** (D1R) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-day-1-retention`
- **Name:** Day 1 Retention
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** D1R

## 2. Definition

Within Gaming, Day 1 Retention (D1R) is used to gauge the retention of customers, users, or assets over time. The formula is Players Returning on Day 1 / New Player Cohort - reported in percent (%). It is a standard measure in the Gaming sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of a new-player cohort active on day one - the first checkpoint of the game-retention funnel, and the harshest: day 1 measures whether the first session delivered a reason to return, and industry benchmarks put good performance at a minority of installs - the majority of downloaded games never get a second session. Its strategic significance is the onboarding verdict: first-session experience (tutorial length, first-game feel, technical performance, early fun) determines it, and improving day 1 is the highest-leverage optimization in mobile gaming because every later metric inherits it multiplicatively. The honest analysis is channel-split: retention varies by acquisition source (organic installs retain better than paid, incentivized traffic worst), so day-1 trends move with marketing mix as much as with product quality - the confound that makes cohort-by-source reads the only honest ones. Read with the first-session-funnel: drop points between install, first-open, and first-match each diagnose different failures.

## Formula

```
D1R = Players Returning on Day 1 / New Player Cohort
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 707 (batch 2)
