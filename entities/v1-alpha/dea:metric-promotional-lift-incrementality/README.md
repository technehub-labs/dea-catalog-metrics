# dea:metric-promotional-lift-incrementality

Candidate Performance Metric record for **Promotional Lift Incrementality** (PLI-MK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-promotional-lift-incrementality`
- **Name:** Promotional Lift Incrementality
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PLI-MK

## 2. Definition

Promotional Lift Incrementality (PLI-MK) addresses the economic value created or preserved and is a fixture of marketing & advertising standard measures (deep dive) reporting. The formula is Incremental Revenue vs Holdout / Promotional Spend - reported in ratio (x:1 or x). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the truly incremental sales caused by promotions versus baseline and pull-forward. Promotions without incrementality are margin donated to existing demand. Lift measured against flat baselines ignores seasonality. Read with markdown cost ratio and price elasticity of demand.

## Formula

```
PLI-MK = Incremental Revenue vs Holdout / Promotional Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing_advertising_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4352 (batch 11)
