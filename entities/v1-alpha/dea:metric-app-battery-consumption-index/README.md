# dea:metric-app-battery-consumption-index

Candidate Performance Metric record for **App Battery Consumption Index** (ABCI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-app-battery-consumption-index`
- **Name:** App Battery Consumption Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ABCI

## 2. Definition

App Battery Consumption Index (ABCI) captures the quality of outputs and outcomes for organizations tracking mobile & client development. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Battery Drain per Hour of Active Use vs Category Benchmark - reported in index (0-100 or normalized). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Software sector.

## Formula

```
Battery Drain per Hour of Active Use vs Category Benchmark
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mobile_client_development
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3257 (batch 7)
