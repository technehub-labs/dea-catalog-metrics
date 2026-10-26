# dea:metric-market-share-growth

Candidate Performance Metric record for **Market Share Growth** (MSG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-market-share-growth`
- **Name:** Market Share Growth
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MSG

## 2. Definition

A Strategy & Portfolio indicator, Market Share Growth (MSG) quantifies growth over time. It is defined as (Market Share_current - Market Share_prior) / Market Share_prior; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Period change in market share - the momentum form of the position metric, and often the more diagnostic one because share changes decompose into share-of-coverage and share-of-preference, which have opposite remedies. Growing share on flat coverage means the offer is winning; growing share bought with distribution expansion is coverage, not preference, and reverses when spending stops. The strategic significance is the tie to the share-of-voice relationship: consistent small gains compound into the leadership flywheel that market-share economics rewards, which is why challenger brands manage annual share-point targets rather than absolute position. The measurement requirement is a consistent market series - share trends computed against shifting market definitions measure the definitions, not the firm - and volume share and value share diverge whenever price positioning changes, which is itself diagnostic.

## Formula

```
(Market Share_current - Market Share_prior) / Market Share_prior
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** strategy_portfolio

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 365 (batch 1)
