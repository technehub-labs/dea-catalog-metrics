# dea:metric-cloud-migration-readiness

Candidate Performance Metric record for **Cloud Migration Readiness** (CMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cloud-migration-readiness`
- **Name:** Cloud Migration Readiness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CMR

## 2. Definition

A Enterprise Architecture indicator, Cloud Migration Readiness (CMR) quantifies capability maturity or development. Its calculation is Applications Assessed Migration-Ready / Applications in Scope, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of applications assessed and prepared for cloud migration. It matters because readiness determines migration velocity and overrun risk. Readiness can be scored generously to hit migration schedule targets. Read with Migration Rework and post-migration performance incidents to confirm readiness was real.

## Formula

```
CMR = Applications Assessed Migration-Ready / Applications in Scope
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** enterprise_architecture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1353 (batch 5)
