# dea:metric-data-quality-trend-index

Candidate Performance Metric record for **Data Quality Trend Index** (DQTI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-quality-trend-index`
- **Name:** Data Quality Trend Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DQTI

## 2. Definition

A Data Quality Management indicator, Data Quality Trend Index (DQTI) quantifies the quality of outputs and outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Period-over-Period Composite Quality Score Change; the result is stated in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the direction of aggregate data quality over time. Trend reveals whether the quality program is winning or merely measuring. A flat trend after heavy investment signals structural causes (source systems) unaddressed. Read with critical data element quality index and cost of poor data quality.

## Formula

```
DQTI = Period-over-Period Composite Quality Score Change
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3627 (batch 8)
