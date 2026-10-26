# dea:metric-thermal-energy-per-tonne-clinker

Candidate Performance Metric record for **Thermal Energy per Tonne Clinker** (TETC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-thermal-energy-per-tonne-clinker`
- **Name:** Thermal Energy per Tonne Clinker
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TETC

## 2. Definition

A Cement & Building Materials indicator, Thermal Energy per Tonne Clinker (TETC) quantifies how efficiently resources are converted into outputs. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Heat Consumed / Clinker Tonnes, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Manufacturing.

## 3. Context

Measures kiln fuel energy per unit of clinker. It is the operating-cost and emissions core of cement manufacturing, and specific heat consumption differences between plants explain most cost gaps in the industry. Read alongside alternative fuel substitution, since fuel type changes shift both energy and emissions accounting. Read with kiln availability (Deep Dive) and clinker factor for the full efficiency picture.

## Formula

```
Heat Consumed / Clinker Tonnes
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cement_building_materials
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1866 (batch 6)
