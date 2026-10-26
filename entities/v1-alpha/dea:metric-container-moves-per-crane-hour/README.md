# dea:metric-container-moves-per-crane-hour

Candidate Performance Metric record for **Container Moves per Crane Hour** (CMCH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-container-moves-per-crane-hour`
- **Name:** Container Moves per Crane Hour
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CMCH

## 2. Definition

Container Moves per Crane Hour (CMCH) captures the utilization or availability of capacity for organizations tracking maritime & shipping. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Container Moves / Crane Operating Hours - reported in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Maritime & shipping sector.

## Formula

```
CMCH = Container Moves / Crane Operating Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 981 (batch 3)
