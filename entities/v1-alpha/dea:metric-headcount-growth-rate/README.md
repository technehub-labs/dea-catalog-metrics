# dea:metric-headcount-growth-rate

Candidate Performance Metric record for **Headcount Growth Rate** (HGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-headcount-growth-rate`
- **Name:** Headcount Growth Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HGR

## 2. Definition

A Human Resources indicator, Headcount Growth Rate (HGR) quantifies growth over time. It is defined as (Headcount_current - Headcount_prior) / Headcount_prior; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Period growth in employee numbers - the metric through which the expansion narrative becomes visible in the cost base before it shows anywhere else. Strategic reading is always against output: headcount growing 20 percent with revenue growing 25 is scaling; the reverse is hiring ahead of a growth story that has not arrived, which is how burn multiples deteriorate quietly. It is also the earliest controllable signal in a downturn - companies cut hiring months before they cut people - which makes the rate a forward indicator that markets and employees both decode. The fine print matters: the metric should separate employee growth from contractor conversion and include the attrition-adjusted net figure, since gross hiring can double the impression of expansion.

## Formula

```
(Headcount_current - Headcount_prior) / Headcount_prior
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 150 (batch 1)
