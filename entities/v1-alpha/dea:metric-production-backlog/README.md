# dea:metric-production-backlog

Candidate Performance Metric record for **Production Backlog** (PBL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-production-backlog`
- **Name:** Production Backlog
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PBL

## 2. Definition

Production Backlog (PBL) addresses the utilization or availability of capacity and is a fixture of manufacturing reporting. It is computed as Open Production Orders Awaiting Start, expressed in count (items per period). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Manufacturing.

## Formula

```
Open Production Orders Awaiting Start
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 261 (batch 1)
