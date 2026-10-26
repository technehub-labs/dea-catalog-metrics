# dea:metric-replenishment-lead-time-adherence

Candidate Performance Metric record for **Replenishment Lead Time Adherence** (RLTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-replenishment-lead-time-adherence`
- **Name:** Replenishment Lead Time Adherence
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RLTA

## 2. Definition

Within Sales & Operations Planning, Replenishment Lead Time Adherence (RLTA) is used to gauge conformance to standards, plans, or obligations. It is computed as Replenishments within Planned Lead Time / Replenishments, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
RLTA = Replenishments within Planned Lead Time / Replenishments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1293 (batch 5)
