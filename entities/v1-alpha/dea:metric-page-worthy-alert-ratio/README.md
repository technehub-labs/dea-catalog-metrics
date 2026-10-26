# dea:metric-page-worthy-alert-ratio

Candidate Performance Metric record for **Page-Worthy Alert Ratio** (PWAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-page-worthy-alert-ratio`
- **Name:** Page-Worthy Alert Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PWAR

## 2. Definition

Page-Worthy Alert Ratio (PWAR) addresses how efficiently resources are converted into outputs and is a fixture of observability & site reliability engineering reporting. It is defined as Pages Meeting Paging Criteria / Pages Sent; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Pages Meeting Paging Criteria / Pages Sent
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2869 (batch 7)
