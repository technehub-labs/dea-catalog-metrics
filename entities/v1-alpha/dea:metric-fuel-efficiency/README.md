# dea:metric-fuel-efficiency

Candidate Performance Metric record for **Fuel Efficiency** (FUE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fuel-efficiency`
- **Name:** Fuel Efficiency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FUE

## 2. Definition

Fuel Efficiency (FUE) measures how efficiently resources are converted into outputs in the Logistics & Transportation domain. The formula is Distance Traveled / Fuel Consumed - reported in ratio (x:1 or x). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Logistics sector.

## Formula

```
Distance Traveled / Fuel Consumed
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 204 (batch 1)
