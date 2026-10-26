# dea:metric-yield-rate

Candidate Performance Metric record for **Yield Rate** (YR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-yield-rate`
- **Name:** Yield Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** YR

## 2. Definition

Within Manufacturing, Yield Rate (YR) is used to gauge the quality of outputs and outcomes. The formula is Good Units Produced / Units Started - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Manufacturing sector.

## Formula

```
Good Units Produced / Units Started
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 248 (batch 1)
