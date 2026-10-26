# dea:metric-process-automation-ratio-deep-dive

Candidate Performance Metric record for **Process Automation Ratio (Deep Dive)** (PAR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-automation-ratio-deep-dive`
- **Name:** Process Automation Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PAR-D

## 2. Definition

Process Automation Ratio (Deep Dive) (PAR-D) addresses how efficiently resources are converted into outputs and is a fixture of balanced scorecard - internal process perspective reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Automated Steps / Total Process Steps; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of process steps executed without manual human handling. Automation is the durable path to unit-cost reduction and consistency. Automating a broken process just makes defects arrive faster. Read with process cost per transaction and first-pass yield trend.

## Formula

```
Automated Steps / Total Process Steps
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_internal_process_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3085 (batch 7)
