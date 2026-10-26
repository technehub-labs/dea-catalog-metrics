# dea:metric-settlement-timeliness

Candidate Performance Metric record for **Settlement Timeliness** (STL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-settlement-timeliness`
- **Name:** Settlement Timeliness
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** STL

## 2. Definition

A Payments & Fintech indicator, Settlement Timeliness (STL) quantifies the quality of outputs and outcomes. It is defined as Settlements Completed by Expected Date / Settlements Due; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Payments & fintech, it is a recognized element of the standard performance toolkit.

## Formula

```
Settlements Completed by Expected Date / Settlements Due
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 779 (batch 2)
