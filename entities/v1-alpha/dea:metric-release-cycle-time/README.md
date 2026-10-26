# dea:metric-release-cycle-time

Candidate Performance Metric record for **Release Cycle Time** (RCLT-RM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-release-cycle-time`
- **Name:** Release Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RCLT-RM

## 2. Definition

A Release Management & Environments indicator, Release Cycle Time (RCLT-RM) quantifies how efficiently resources are converted into outputs. It is defined as Days between Consecutive Production Releases; the result is stated in days. It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the elapsed time from code complete or feature start to production availability. Shorter cycles compound: faster feedback, smaller batches, lower risk per release. Cutting cycle time by reducing quality gates merely converts cycle time into incident time. Read with lead time for changes and change failure rate.

## Formula

```
Days between Consecutive Production Releases
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** release_management_environments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2732 (batch 7)
