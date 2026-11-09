# dea:metric-requirements-stability-index

Candidate Performance Metric record for **Requirements Stability Index** (RSI-RE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-requirements-stability-index`
- **Name:** Requirements Stability Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RSI-RE

## 2. Definition

A Requirements Engineering & Product Discovery indicator, Requirements Stability Index (RSI-RE) quantifies exposure to adverse outcomes. The formula is Unchanged Requirements after Baseline / Baseline - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
RSI-RE = Unchanged Requirements after Baseline / Baseline
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** requirements_engineering_product_discovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2603 (batch 7)
