# dea:metric-cardinality-cost-ratio

Candidate Performance Metric record for **Cardinality Cost Ratio** (CARDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cardinality-cost-ratio`
- **Name:** Cardinality Cost Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CARDR

## 2. Definition

Within SRE & Observability Standard Measures, Cardinality Cost Ratio (CARDR) is used to gauge how efficiently resources are converted into outputs. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Observability Spend / Revenue Streamed through Platform, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Software.

## Formula

```
CARDR = Observability Spend / Revenue Streamed through Platform
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4384 (batch 11)
