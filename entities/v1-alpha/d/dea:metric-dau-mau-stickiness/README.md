# dea:metric-dau-mau-stickiness

Candidate Performance Metric record for **DAU/MAU Stickiness** (STICK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dau-mau-stickiness`
- **Name:** DAU/MAU Stickiness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** STICK

## 2. Definition

A Product Management indicator, DAU/MAU Stickiness (STICK) quantifies the engagement or satisfaction of the people involved. It is computed as Daily Active Users / Monthly Active Users, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Daily actives as a share of monthly actives - the fraction-of-your-audience-comes-daily ratio, which became the standard stickiness shorthand of consumer product analytics. Its strategic significance is the frequency taxonomy it encodes: messaging and social products run above 50 percent because they sit in daily routines, utility and content products run in the teens, and the ratio places a product on the frequency spectrum, which predicts what growth levers and monetization models are even possible. The metric's failure mode is treating it as a universal target - maximizing stickiness on a product whose job is episodic (travel, tax, real estate) is optimizing the wrong job - which is why the honest read is against category benchmarks and against the product's intended use frequency, not against the messaging-app ceiling.

## Formula

```
STICK = Daily Active Users / Monthly Active Users
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 552 (batch 1)
