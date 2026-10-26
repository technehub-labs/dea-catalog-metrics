# dea:metric-population-stability-index-model

Candidate Performance Metric record for **Population Stability Index (Model)** (PSIM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-population-stability-index-model`
- **Name:** Population Stability Index (Model)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PSIM

## 2. Definition

Population Stability Index (Model) (PSIM) captures exposure to adverse outcomes for organizations tracking statistical model performance diagnostics. It is defined as Divergence of Score Distribution vs Development Sample; the result is stated in index (0-100 or normalized). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
PSIM = Divergence of Score Distribution vs Development Sample
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4066 (batch 9)
