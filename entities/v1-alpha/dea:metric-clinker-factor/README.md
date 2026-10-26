# dea:metric-clinker-factor

Candidate Performance Metric record for **Clinker Factor** (CF-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-clinker-factor`
- **Name:** Clinker Factor
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CF-C

## 2. Definition

A Cement & Building Materials indicator, Clinker Factor (CF-C) quantifies environmental and social sustainability performance. Its calculation is Clinker Mass / Cement Mass, measured in ratio (x:1 or x). It originates from and is most used in Manufacturing practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of clinker in finished cement. It is the central environmental and cost lever of cement: clinker production is the emissions hotspot, and every percentage point substituted with supplementary materials cuts CO2 directly. Substitution limits are set by product standard requirements, so read with strength-grade mix and regional SCM availability. Read with thermal energy per tonne clinker and emissions intensity.

## Formula

```
Clinker Mass / Cement Mass
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** sustainability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1864 (batch 6)
