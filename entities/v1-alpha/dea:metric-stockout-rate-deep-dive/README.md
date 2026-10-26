# dea:metric-stockout-rate-deep-dive

Candidate Performance Metric record for **Stockout Rate (Deep Dive)** (SORD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stockout-rate-deep-dive`
- **Name:** Stockout Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SORD

## 2. Definition

A Supply Chain Standard Measures (Deep Dive) indicator, Stockout Rate (Deep Dive) (SORD) quantifies the quality of outputs and outcomes. Its calculation is Demand Occasions Unfilled / Demand Occasions, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
SORD = Demand Occasions Unfilled / Demand Occasions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4265 (batch 10)
