# dea:metric-process-cycle-efficiency-deep-dive

Candidate Performance Metric record for **Process Cycle Efficiency (Deep Dive)** (PCED) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-cycle-efficiency-deep-dive`
- **Name:** Process Cycle Efficiency (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PCED

## 2. Definition

Process Cycle Efficiency (Deep Dive) (PCED) captures how efficiently resources are converted into outputs for organizations tracking operating model & process health deep dive. Its calculation is Value-Added Time / Total Lead Time, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Value-Added Time / Total Lead Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operating_model_process_health_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3497 (batch 7)
