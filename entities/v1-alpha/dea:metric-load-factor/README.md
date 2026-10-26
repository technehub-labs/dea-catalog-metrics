# dea:metric-load-factor

Candidate Performance Metric record for **Load Factor** (LF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-load-factor`
- **Name:** Load Factor
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LF

## 2. Definition

Load Factor (LF) measures how efficiently resources are converted into outputs in the Logistics & Transportation domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Occupied Capacity / Available Capacity, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Logistics practice.

## 3. Context

Measures how full vehicles or capacity are relative to maximum capacity. It matters because revenue per trip scales directly with how much paying weight or volume is carried. Overloading to boost the factor risks safety violations, fines, and damage claims. Read with Empty Miles Rate and Freight Cost per Unit to see whether high load factors reflect good planning or risky squeezing.

## Formula

```
Occupied Capacity / Available Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 201 (batch 1)
