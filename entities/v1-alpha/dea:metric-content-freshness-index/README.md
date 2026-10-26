# dea:metric-content-freshness-index

Candidate Performance Metric record for **Content Freshness Index** (CFI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-content-freshness-index`
- **Name:** Content Freshness Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CFI

## 2. Definition

Content Freshness Index (CFI) measures conformance to standards, plans, or obligations in the Digital Product & Web Operations domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Pages Updated within Review Cadence / Total Pages; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CFI = Pages Updated within Review Cadence / Total Pages
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** digital_product_web_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1083 (batch 4)
