# dea:metric-semantic-layer-coverage

Candidate Performance Metric record for **Semantic Layer Coverage** (SLC-DS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-semantic-layer-coverage`
- **Name:** Semantic Layer Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SLC-DS

## 2. Definition

Semantic Layer Coverage (SLC-DS) addresses capability maturity or development and is a fixture of data science & analytics operations reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Metrics Defined in Semantic Layer / Total Governed Metrics, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of key business metrics and dimensions defined once in a governed semantic layer. The semantic layer is the definition-integrity infrastructure of analytics: without it, every team reimplements revenue or active-customer calculations, and the numbers diverge. Coverage by metric criticality matters more than count, since the metrics in executive reporting are where divergence costs most. Read with certified data source utilization (Deep Dive) and metric-definition governance.

## Formula

```
Metrics Defined in Semantic Layer / Total Governed Metrics
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_science_analytics_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2598 (batch 7)
