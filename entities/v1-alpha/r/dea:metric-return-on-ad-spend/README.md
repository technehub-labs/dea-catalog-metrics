# dea:metric-return-on-ad-spend

Candidate Performance Metric record for **Return on Ad Spend** (ROAS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-on-ad-spend`
- **Name:** Return on Ad Spend
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ROAS

## 2. Definition

Within Marketing Attribution & Analytics, Return on Ad Spend (ROAS) is used to gauge the economic value created or preserved. It is computed as Attributed Revenue / Ad Spend, expressed in ratio (x:1 or x). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures revenue (or margin) generated per unit of advertising spend, by channel, campaign, or portfolio. It is the workhorse of marketing economics, but only as honest as its attribution: last-touch ROAS systematically overvalues bottom-funnel channels and undervalues brand and upper-funnel investment. Use margin-based ROAS where possible and platform-reported ROAS only as directional. Read with incrementality rate and marketing mix model alignment.

## Formula

```
ROAS = Attributed Revenue / Ad Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** marketing_attribution_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1493 (batch 5)
