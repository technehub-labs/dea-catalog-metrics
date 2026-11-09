# dea:metric-fuel-burn-variance-per-flight-deep-dive

Candidate Performance Metric record for **Fuel Burn Variance per Flight (Deep Dive)** (FBVF-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fuel-burn-variance-per-flight-deep-dive`
- **Name:** Fuel Burn Variance per Flight (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FBVF-D

## 2. Definition

Fuel Burn Variance per Flight (Deep Dive) (FBVF-D) addresses how efficiently resources are converted into outputs and is a fixture of airline operations (deep dive) reporting. It is defined as Actual Fuel Burn - Flight Plan Fuel / Plan; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. In Airlines, it is a recognized element of the standard performance toolkit.

## Formula

```
FBVF-D = Actual Fuel Burn - Flight Plan Fuel / Plan
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2260 (batch 6)
