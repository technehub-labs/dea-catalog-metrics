# dea:metric-trace-sampling-coverage

Candidate Performance Metric record for **Trace Sampling Coverage** (TSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trace-sampling-coverage`
- **Name:** Trace Sampling Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TSC

## 2. Definition

A Observability & Site Reliability Engineering indicator, Trace Sampling Coverage (TSC) quantifies capability maturity or development. It is computed as Transactions with Distributed Tracing / Transactions, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
TSC = Transactions with Distributed Tracing / Transactions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2866 (batch 7)
