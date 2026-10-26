# dea:metric-flow-efficiency-deep-dive

Candidate Performance Metric record for **Flow Efficiency (Deep Dive)** (FE-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-flow-efficiency-deep-dive`
- **Name:** Flow Efficiency (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FE-D

## 2. Definition

A Agile Delivery & Team Effectiveness indicator, Flow Efficiency (Deep Dive) (FE-D) quantifies how efficiently resources are converted into outputs. It is defined as Active Work Time / Total Lead Time; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures active work time versus total elapsed time for work items. Most items wait the vast majority of their life cycle; flow efficiency exposes the queues. Improving it means removing dependencies and approvals, not pressing people harder. Local flow gains that ignore the end-to-end value stream mislead. Read with flow time and flow load, plus cycle time.

## Formula

```
Active Work Time / Total Lead Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agile_delivery_team_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2996 (batch 7)
