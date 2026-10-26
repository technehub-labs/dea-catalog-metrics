# dea:metric-vegetation-management-compliance-grid

Candidate Performance Metric record for **Vegetation Management Compliance (Grid)** (VMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vegetation-management-compliance-grid`
- **Name:** Vegetation Management Compliance (Grid)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VMC

## 2. Definition

A Utilities Field Operations & Grid indicator, Vegetation Management Compliance (Grid) (VMC) quantifies exposure to adverse outcomes. Its calculation is Spans Treated per Cycle Plan / Planned, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Utilities practice.

## 3. Context

Measures completion of vegetation clearance schedules along power lines. Vegetation contact is a leading cause of utility outages and wildfires, making this compliance metric a public-safety obligation, not an aesthetic one. Compliance by circuit-miles can hide risk concentration, so prioritize by fire-threat and outage-history zones. Read with outage causes and inspection quality assurance findings.

## Formula

```
Spans Treated per Cycle Plan / Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1886 (batch 6)
