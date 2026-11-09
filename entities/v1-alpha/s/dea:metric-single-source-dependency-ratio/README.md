# dea:metric-single-source-dependency-ratio

Candidate Performance Metric record for **Single-Source Dependency Ratio** (SSDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-single-source-dependency-ratio`
- **Name:** Single-Source Dependency Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SSDR

## 2. Definition

Within Strategic Sourcing & Supplier Performance (Deep Dive), Single-Source Dependency Ratio (SSDR) is used to gauge exposure to adverse outcomes. It is computed as Critical Categories with Single Supplier / Critical Categories, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of critical spend resting on single-source suppliers. Single sourcing trades price and continuity risk for convenience. Dependency classified as 'no alternative exists' often means 'no alternative was sought'. Read with concentration risk ratio and dual sourcing coverage.

## Formula

```
SSDR = Critical Categories with Single Supplier / Critical Categories
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** strategic_sourcing_supplier_performance_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3745 (batch 8)
