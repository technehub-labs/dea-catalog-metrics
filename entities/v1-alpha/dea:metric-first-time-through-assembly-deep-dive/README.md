# dea:metric-first-time-through-assembly-deep-dive

Candidate Performance Metric record for **First Time Through - Assembly (Deep Dive)** (FTA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-time-through-assembly-deep-dive`
- **Name:** First Time Through - Assembly (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FTA-D

## 2. Definition

A Automotive Manufacturing (Deep Dive) indicator, First Time Through - Assembly (Deep Dive) (FTA-D) quantifies the quality of outputs and outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Vehicles Passing without Rework / Vehicles; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Automotive, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of vehicles moving through assembly without rework or repair. It is the pure quality-flow metric of automotive production: every vehicle pulled offline for repair costs floor space, labor, and schedule integrity, and FTT below world-class levels signals process instability that volume cannot hide. Track by station and defect type, since Pareto concentration is the improvement lever. Read with supplier PPM - automotive (Deep Dive) and launch quality index (Deep Dive).

## Formula

```
FTA-D = Vehicles Passing without Rework / Vehicles
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2360 (batch 6)
