# dea:metric-power-factor

Candidate Performance Metric record for **Power Factor** (PFE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-power-factor`
- **Name:** Power Factor
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PFE

## 2. Definition

Within Operations Energy Management, Power Factor (PFE) is used to gauge how efficiently resources are converted into outputs. It is computed as Real Power / Apparent Power, expressed in ratio (x:1 or x). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Real Power / Apparent Power
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** operations_energy_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1438 (batch 5)
