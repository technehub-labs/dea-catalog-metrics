# dea:metric-cardinality-growth-control-ratio

Candidate Performance Metric record for **Cardinality Growth Control Ratio** (CGCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cardinality-growth-control-ratio`
- **Name:** Cardinality Growth Control Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CGCR

## 2. Definition

A Observability & Site Reliability Engineering indicator, Cardinality Growth Control Ratio (CGCR) quantifies the utilization or availability of capacity. Its calculation is Metric Cardinality Growth / Headroom Budget, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Values outside the intended band, on either side, warrant investigation.

## Formula

```
CGCR = Metric Cardinality Growth / Headroom Budget
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2881 (batch 7)
