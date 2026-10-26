# dea:metric-paint-shop-first-pass-rate-deep-dive

Candidate Performance Metric record for **Paint Shop First-Pass Rate (Deep Dive)** (PSFP-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-paint-shop-first-pass-rate-deep-dive`
- **Name:** Paint Shop First-Pass Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PSFP-D

## 2. Definition

Paint Shop First-Pass Rate (Deep Dive) (PSFP-D) addresses the quality of outputs and outcomes and is a fixture of automotive manufacturing (deep dive) reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Bodies Passing Paint Inspection / Bodies - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Automotive sector.

## Formula

```
PSFP-D = Bodies Passing Paint Inspection / Bodies
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2366 (batch 6)
