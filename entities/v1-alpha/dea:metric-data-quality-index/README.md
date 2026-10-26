# dea:metric-data-quality-index

Candidate Performance Metric record for **Data Quality Index** (DQI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-quality-index`
- **Name:** Data Quality Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DQI

## 2. Definition

Data Quality Index (DQI) measures the quality of outputs and outcomes in the Data Management & Analytics domain. The formula is Weighted Index of Completeness, Accuracy, Timeliness, Consistency - reported in index (0-100 or normalized). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

A composite score of fitness-for-purpose across data quality dimensions - conventionally completeness, accuracy, consistency, timeliness, validity, and uniqueness, weighted into a single index. Its strategic significance is that data quality is upstream of everything analytic: every model, report, and AI system inherits the errors of its inputs, and the index is the early-warning gauge for that inheritance. The composite structure is both its power and its weakness - a single number makes quality governable at portfolio level, but the weighting is arbitrary, and different applications need different dimensions (a real-time recommendation engine cares about timeliness, a regulatory report cares about accuracy), which is why mature programs publish the index with per-dimension breakdowns. Scored against rules that run continuously rather than point-in-time audits, the index becomes a genuine operating metric instead of an annual reassurance.

## Formula

```
Weighted Index of Completeness, Accuracy, Timeliness, Consistency
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
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 340 (batch 1)
