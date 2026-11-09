# dea:metric-cooling-efficiency-delta-t-compliance

Candidate Performance Metric record for **Cooling Efficiency - Delta-T Compliance** (CEDT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cooling-efficiency-delta-t-compliance`
- **Name:** Cooling Efficiency - Delta-T Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CEDT

## 2. Definition

Cooling Efficiency - Delta-T Compliance (CEDT) measures how efficiently resources are converted into outputs in the Data Centers & Cloud Infrastructure domain. The formula is Airflow Tests Meeting Delta-T Design / Tests - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Technology sector.

## Formula

```
CEDT = Airflow Tests Meeting Delta-T Design / Tests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2142 (batch 6)
