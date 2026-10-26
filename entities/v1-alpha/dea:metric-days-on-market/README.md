# dea:metric-days-on-market

Candidate Performance Metric record for **Days on Market** (DOM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-on-market`
- **Name:** Days on Market
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DOM

## 2. Definition

Days on Market (DOM) captures how efficiently resources are converted into outputs for organizations tracking real estate brokerage. It is defined as Average Days from Listing to Contract; the result is stated in days. In Real estate, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Days on market measures time from listing to contract, and it is the real estate metric that signals pricing accuracy more than demand - a home sitting beyond the market median almost always carries a price the market rejects, since buyers now have perfect price visibility through portals. DOM is a two-way diagnostic: high DOM with eventual sale at near-asking suggests a slow market; high DOM with eventual deep discount confirms overpricing. The strategic use is pricing-discipline: agents who consistently list above market waste their clients' time (and their own carrying-cost exposure). Read with sale-price-to-list-price ratio as the pair that separates pricing realism from negotiation dynamics, and with inventory age distribution to see whether stale listings are clustering.

## Formula

```
DOM = Average Days from Listing to Contract
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** real_estate_brokerage
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1011 (batch 3)
