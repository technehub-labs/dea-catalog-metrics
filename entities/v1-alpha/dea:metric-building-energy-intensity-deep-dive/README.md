# dea:metric-building-energy-intensity-deep-dive

Candidate Performance Metric record for **Building Energy Intensity (Deep Dive)** (BEI-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-building-energy-intensity-deep-dive`
- **Name:** Building Energy Intensity (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BEI-D

## 2. Definition

Building Energy Intensity (Deep Dive) (BEI-D) captures environmental and social sustainability performance for organizations tracking facility management & workplace (deep dive). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Energy / Floor Area; the result is stated in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures energy consumption per unit of area (kWh per square metre), weather-normalized. It is the efficiency and carbon metric of building operations, and normalization integrity is the whole game - unadjusted intensity numbers move with weather, occupancy, and use changes that have nothing to do with performance. Read intensity with occupancy, since low-intensity empty buildings are waste, not efficiency. Read with space utilization rate (Deep Dive) and energy-retrofit project realization.

## Formula

```
Energy / Floor Area
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facility_management_workplace_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2241 (batch 6)
