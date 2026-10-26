# dea:metric-value-added-time-ratio

Candidate Performance Metric record for **Value-Added Time Ratio** (VATR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-value-added-time-ratio`
- **Name:** Value-Added Time Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VATR

## 2. Definition

Value-Added Time Ratio (VATR) addresses how efficiently resources are converted into outputs and is a fixture of process excellence (lean six sigma) reporting. It is defined as Value-Added Process Time / Total Lead Time; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of total process time spent on value-creating work. It matters because it is the lean movement's core waste-revealing metric. Mapping workshops can generously classify waiting or rework as value-added. Read with Process Cycle Efficiency and Wait Time Ratio to confirm classification discipline and target the worst constraints.

## Formula

```
Value-Added Process Time / Total Lead Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_excellence_lean_six_sigma

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1112 (batch 4)
