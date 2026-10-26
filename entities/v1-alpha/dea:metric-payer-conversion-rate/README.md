# dea:metric-payer-conversion-rate

Candidate Performance Metric record for **Payer Conversion Rate** (PCR-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payer-conversion-rate`
- **Name:** Payer Conversion Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PCR-G

## 2. Definition

Payer Conversion Rate (PCR-G) addresses the economic value created or preserved and is a fixture of gaming reporting. The formula is Paying Users / Active Users - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Gaming sector.

## 3. Context

The share of active players making at least one purchase in a period - the conversion metric of free-to-play, and the strategic question of the model: the majority of revenue comes from the few who convert, so the funnel from player to payer is where the product's monetization design either works or fails. Its significance is the first-purchase moment: conversion is dominated by the early experience - the tutorial-to-first-offer window, the value proposition of the starter pack - and conversion-rate analysis by cohort, day, and offer placement is the core of live-ops optimization. The honest read separates willingness from friction: players who never see value in paying (design question) differ from players who wanted to pay and were blocked (payment-method coverage, price-point availability - the localization question). Read with retention: conversion mechanics that churn players before purchase damage the player base that conversion exists to monetize, which is why the metric is always read with the retention companion.

## Formula

```
Paying Users / Active Users
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 705 (batch 2)
