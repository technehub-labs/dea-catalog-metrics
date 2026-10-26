# dea:metric-toil-ratio

Candidate Performance Metric record for **Toil Ratio** (TOILR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-toil-ratio`
- **Name:** Toil Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TOILR

## 2. Definition

Toil Ratio (TOILR) addresses how efficiently resources are converted into outputs and is a fixture of sre & observability standard measures reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Toil Hours / Total Engineering Hours, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Software practice.

## Formula

```
Toil Hours / Total Engineering Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4381 (batch 11)
