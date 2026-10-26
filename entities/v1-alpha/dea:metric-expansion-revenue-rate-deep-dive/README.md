# dea:metric-expansion-revenue-rate-deep-dive

Candidate Performance Metric record for **Expansion Revenue Rate (Deep Dive)** (EXPRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-expansion-revenue-rate-deep-dive`
- **Name:** Expansion Revenue Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EXPRD

## 2. Definition

A Unit Economics & Growth (Deep Dive) indicator, Expansion Revenue Rate (Deep Dive) (EXPRD) quantifies growth over time. It is computed as Expansion MRR / Total Prior MRR, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Software.

## 3. Context

Measures revenue growth from existing customers (upsell, cross-sell, usage). Expansion is the highest-margin growth available. Expansion driven by unilateral price rises rather than delivered value churns later. Read with net dollar retention (Deep Dive) and net revenue retention.

## Formula

```
EXPRD = Expansion MRR / Total Prior MRR
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4168 (batch 9)
