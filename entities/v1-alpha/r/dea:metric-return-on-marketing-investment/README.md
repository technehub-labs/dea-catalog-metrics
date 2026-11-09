# dea:metric-return-on-marketing-investment

Candidate Performance Metric record for **Return on Marketing Investment** (ROMI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-on-marketing-investment`
- **Name:** Return on Marketing Investment
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ROMI

## 2. Definition

Return on Marketing Investment (ROMI) measures the economic value created or preserved in the Marketing domain. It is computed as (Attributable Revenue - Marketing Spend) / Marketing Spend, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Incremental profit or revenue attributable to marketing, divided by the marketing spend - the accountability metric that moved marketing from the arts budget to the capital allocation conversation. Its strategic difficulty is the word incremental: attribution models from last-click to media-mix modeling produce different ROMI for the same campaign, and the honest answer sits in incrementality testing. The metric's real use is comparative and marginal - ranking channels by ROMI to allocate the next dollar - rather than absolute; a blended ROMI across all marketing answers a question no one asks, because the decision is never all-spend versus none. Long-term brand investment deliberately depresses near-term ROMI, so penalizing it on a quarterly ROMI ledger is how companies quietly defund their future pricing power.

## Formula

```
ROMI = (Attributable Revenue - Marketing Spend) / Marketing Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 104 (batch 1)
