# dea:metric-asset-health-index-deep-dive

Candidate Performance Metric record for **Asset Health Index (Deep Dive)** (AHID) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-health-index-deep-dive`
- **Name:** Asset Health Index (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AHID

## 2. Definition

Within Reliability & Maintainability Engineering (Deep Dive), Asset Health Index (Deep Dive) (AHID) is used to gauge exposure to adverse outcomes. The formula is Composite Condition Score of Asset Fleet - reported in index (0-100 or normalized). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures composite asset condition from condition monitoring, inspection, and history. The index prioritizes scarce maintenance on the assets nearest failure. Index weighting choices drive the ranking more than the data does. Read with remaining useful life prediction accuracy and maintenance backlog age.

## Formula

```
Composite Condition Score of Asset Fleet
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** capability
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4111 (batch 9)
