# dea:metric-master-data-hierarchy-accuracy

Candidate Performance Metric record for **Master Data Hierarchy Accuracy** (MDHA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-master-data-hierarchy-accuracy`
- **Name:** Master Data Hierarchy Accuracy
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MDHA

## 2. Definition

A Master Data Management indicator, Master Data Hierarchy Accuracy (MDHA) quantifies the quality of outputs and outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Hierarchy Structures Matching Verified Reality / Hierarchies Sampled; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether customer, product, and org hierarchies correctly reflect real-world relationships. Hierarchy errors poison roll-ups: every report aggregated on them is wrong. Accuracy sampled only on new records hides legacy corruption. Read with master data coverage rate and hierarchy maintenance cycle time.

## Formula

```
Hierarchy Structures Matching Verified Reality / Hierarchies Sampled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3641 (batch 8)
