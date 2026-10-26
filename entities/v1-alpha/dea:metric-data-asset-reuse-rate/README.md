# dea:metric-data-asset-reuse-rate

Candidate Performance Metric record for **Data Asset Reuse Rate** (DARR-DS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-asset-reuse-rate`
- **Name:** Data Asset Reuse Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DARR-DS

## 2. Definition

Data Asset Reuse Rate (DARR-DS) measures how efficiently resources are converted into outputs in the Data Science & Analytics Operations domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Reusable Data Assets Reused / Published Assets, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how often enterprise data assets (tables, features, metrics) are reused across teams and use cases. It is the compounding-asset metric of data strategy: reuse amortizes creation cost, enforces consistency, and signals which assets are actually valuable versus maintained out of habit. Reuse tracking requires lineage instrumentation to be credible. Read with semantic layer coverage (Deep Dive) and cost-per-use economics of maintained assets.

## Formula

```
Reusable Data Assets Reused / Published Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_science_analytics_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2593 (batch 7)
