# dea:metric-contribution-margin-per-unit-deep-dive

Candidate Performance Metric record for **Contribution Margin per Unit (Deep Dive)** (CMPUD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contribution-margin-per-unit-deep-dive`
- **Name:** Contribution Margin per Unit (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CMPUD

## 2. Definition

Within Unit Economics & Growth (Deep Dive), Contribution Margin per Unit (Deep Dive) (CMPUD) is used to gauge the economic value created or preserved. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as (Price - Variable Cost) per Unit, expressed in currency per unit. Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Software.

## Formula

```
CMPUD = (Price - Variable Cost) per Unit
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4161 (batch 9)
