# dea:metric-score-distribution-drift

Candidate Performance Metric record for **Score Distribution Drift** (SDDM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-score-distribution-drift`
- **Name:** Score Distribution Drift
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SDDM

## 2. Definition

Score Distribution Drift (SDDM) captures exposure to adverse outcomes for organizations tracking statistical model performance diagnostics. The formula is Period Change in Score Population Moments vs Baseline - reported in percent (%). It is a standard measure in the Software sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Period Change in Score Population Moments vs Baseline
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4073 (batch 9)
