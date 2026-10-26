# dea:metric-yield-gap-ratio-deep-dive

Candidate Performance Metric record for **Yield Gap Ratio (Deep Dive)** (YGR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-yield-gap-ratio-deep-dive`
- **Name:** Yield Gap Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** YGR-D

## 2. Definition

Within Agriculture & Agronomy (Deep Dive), Yield Gap Ratio (Deep Dive) (YGR-D) is used to gauge the quality of outputs and outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Actual Yield - Attainable Yield / Attainable Yield - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Agriculture sector.

## 3. Context

Compares achieved yields against attainable yields for the same agro-climatic zone and input system. It is the strategy metric of agriculture: it quantifies the improvement headroom that genetics, agronomy, and practice could still unlock, and it prioritizes where intervention pays. Attainable-yield benchmarks are estimates, so definition discipline matters more than precision. Read with crop yield per hectare (Deep Dive) trends and input use efficiency - nitrogen.

## Formula

```
Actual Yield - Attainable Yield / Attainable Yield
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_agronomy_deep_dive
- **Sector:** agriculture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2313 (batch 6)
