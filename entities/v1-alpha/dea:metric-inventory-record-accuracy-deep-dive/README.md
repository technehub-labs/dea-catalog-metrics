# dea:metric-inventory-record-accuracy-deep-dive

Candidate Performance Metric record for **Inventory Record Accuracy (Deep Dive)** (IRA-DD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-inventory-record-accuracy-deep-dive`
- **Name:** Inventory Record Accuracy (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IRA-DD

## 2. Definition

Within Supply Chain Standard Measures (Deep Dive), Inventory Record Accuracy (Deep Dive) (IRA-DD) is used to gauge the quality of outputs and outcomes. Its calculation is Bins Matching System Count / Bins Sampled, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Bins Matching System Count / Bins Sampled
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4264 (batch 10)
