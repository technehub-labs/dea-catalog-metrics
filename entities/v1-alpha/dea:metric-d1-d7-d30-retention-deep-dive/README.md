# dea:metric-d1-d7-d30-retention-deep-dive

Candidate Performance Metric record for **D1 / D7 / D30 Retention (Deep Dive)** (RET-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-d1-d7-d30-retention-deep-dive`
- **Name:** D1 / D7 / D30 Retention (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RET-D

## 2. Definition

D1 / D7 / D30 Retention (Deep Dive) (RET-D) measures the retention of customers, users, or assets over time in the Gaming Development & Live Operations domain. It is computed as Returning Players on Day N / New Players, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Gaming.

## 3. Context

Measures the share of new players returning on day one, seven, and thirty after install. These curves are the canonical health metrics of game design: weak D1 is a product-quality signal, weak D30 a content-depth or progression signal, and the curves together locate where players decide the game is not for them. Cohort by acquisition source, since paid installs retain differently from organic. Read with DAU-to-MAU stickiness (Deep Dive) for the engaged-base picture.

## Formula

```
RET-D = Returning Players on Day N / New Players
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
- **Domain:** gaming_development_live_operations
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1983 (batch 6)
