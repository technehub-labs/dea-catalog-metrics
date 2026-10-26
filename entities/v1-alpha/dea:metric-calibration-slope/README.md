# dea:metric-calibration-slope

Candidate Performance Metric record for **Calibration Slope** (CALS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-calibration-slope`
- **Name:** Calibration Slope
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CALS

## 2. Definition

Calibration Slope (CALS) captures the quality of outputs and outcomes for organizations tracking statistical model performance diagnostics. Its calculation is Slope of Observed vs Predicted Probability Fit, measured in ratio (x:1 or x). It provides the day-to-day signal that a process is running as designed. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It originates from and is most used in Software practice.

## Formula

```
Slope of Observed vs Predicted Probability Fit
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4065 (batch 9)
