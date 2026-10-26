# dea:metric-strip-ratio-deep-dive

Candidate Performance Metric record for **Strip Ratio (Deep Dive)** (SR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-strip-ratio-deep-dive`
- **Name:** Strip Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SR-D

## 2. Definition

Strip Ratio (Deep Dive) (SR-D) addresses how efficiently resources are converted into outputs and is a fixture of metals & mining operations (deep dive) reporting. It is defined as Waste Tonnes / Ore Tonnes; the result is stated in ratio (x:1 or x). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. In Metals & Mining, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures waste tonnes moved per ore tonne in open-pit operations. It is the cost-structure dial of surface mining: strip ratio deteriorations raise unit cost steeply, and mine plans often hide rising ratios in later years. Read the life-of-mine strip profile, not the current-year ratio, and watch for ratios suppressed by high-grade phases that front-load value. Read with mining cost per tonne and reserve replacement planning.

## Formula

```
Waste Tonnes / Ore Tonnes
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** metals_mining_operations_deep_dive
- **Sector:** metals_mining

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1841 (batch 6)
