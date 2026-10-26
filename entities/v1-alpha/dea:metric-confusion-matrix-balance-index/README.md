# dea:metric-confusion-matrix-balance-index

Candidate Performance Metric record for **Confusion Matrix Balance Index** (CMBI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-confusion-matrix-balance-index`
- **Name:** Confusion Matrix Balance Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CMBI

## 2. Definition

Confusion Matrix Balance Index (CMBI) addresses the quality of outputs and outcomes and is a fixture of statistical model performance diagnostics reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Symmetry of Error Types at Operating Threshold, measured in index (0-100 or normalized). The objective is neither maximization nor minimization but staying within an agreed operating band. It originates from and is most used in Software practice.

## Formula

```
Symmetry of Error Types at Operating Threshold
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4071 (batch 9)
