# dea:metric-process-maturity-score-deep-dive

Candidate Performance Metric record for **Process Maturity Score (Deep Dive)** (PMSD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-maturity-score-deep-dive`
- **Name:** Process Maturity Score (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PMSD

## 2. Definition

Process Maturity Score (Deep Dive) (PMSD) measures capability maturity or development in the Operating Model & Process Health Deep Dive domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is CMMI-Style Maturity Rating across Core Processes, measured in score (points). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures aggregate process capability against a maturity model (e.g., CMMI-style levels). Maturity predicts how consistently a process can hold its performance under stress. Self-assessed maturity inflates by roughly a level versus independent assessment. Read with capability maturity assessment currency and process effectiveness index.

## Formula

```
PMSD = CMMI-Style Maturity Rating across Core Processes
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operating_model_process_health_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3496 (batch 7)
