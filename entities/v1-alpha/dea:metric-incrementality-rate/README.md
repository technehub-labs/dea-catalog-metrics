# dea:metric-incrementality-rate

Candidate Performance Metric record for **Incrementality Rate** (INCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incrementality-rate`
- **Name:** Incrementality Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** INCR

## 2. Definition

Within Marketing Attribution & Analytics, Incrementality Rate (INCR) is used to gauge the economic value created or preserved. It is defined as Incremental Conversions from Test vs Control / Test Conversions; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of attributed marketing outcomes that were truly caused - incremental above a holdout baseline - rather than simply correlated with exposure. It is the honesty layer over attribution and ROAS: most last-touch credited sales would have happened anyway. Measurement requires controlled experiments or geo-testing, which are costly but the only defensible ground truth. Read with return on ad spend and marketing mix model alignment.

## Formula

```
INCR = Incremental Conversions from Test vs Control / Test Conversions
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
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** marketing_attribution_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1491 (batch 5)
