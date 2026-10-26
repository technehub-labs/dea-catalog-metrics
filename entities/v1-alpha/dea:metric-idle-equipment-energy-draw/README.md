# dea:metric-idle-equipment-energy-draw

Candidate Performance Metric record for **Idle Equipment Energy Draw** (IED) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-idle-equipment-energy-draw`
- **Name:** Idle Equipment Energy Draw
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IED

## 2. Definition

Idle Equipment Energy Draw (IED) captures how efficiently resources are converted into outputs for organizations tracking operations energy management. It is computed as Energy Consumed by Idle Equipment / Total Energy, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Energy Consumed by Idle Equipment / Total Energy
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** operations_energy_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1433 (batch 5)
