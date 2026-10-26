# dea:metric-wafer-fab-cycle-time-deep-dive

Candidate Performance Metric record for **Wafer Fab Cycle Time (Deep Dive)** (WFCT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wafer-fab-cycle-time-deep-dive`
- **Name:** Wafer Fab Cycle Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WFCT-D

## 2. Definition

Wafer Fab Cycle Time (Deep Dive) (WFCT-D) addresses how efficiently resources are converted into outputs and is a fixture of semiconductor manufacturing (deep dive) reporting. It is defined as Days from Wafer Start to Wafer Out; the result is stated in days. Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Semiconductors, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures elapsed time from wafer start to completion in fabrication. Cycle time is the strategy metric of semiconductor manufacturing: fabs are fixed-cost machines with astronomical capital intensity, and cycle time reductions simultaneously free capacity (WIP physics) and shorten customer lead times. Cycle-time gains from cherry-picking hot lots degrade the baseline product flow. Read with wafer fab WIP levels and on-time delivery - wafer commitments (Deep Dive).

## Formula

```
Days from Wafer Start to Wafer Out
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_manufacturing_deep_dive
- **Sector:** semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2372 (batch 6)
