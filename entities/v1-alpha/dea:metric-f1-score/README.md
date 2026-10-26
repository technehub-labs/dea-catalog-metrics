# dea:metric-f1-score

Candidate Performance Metric record for **F1 Score** (F1SC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-f1-score`
- **Name:** F1 Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** F1SC

## 2. Definition

Within Statistical Model Performance Diagnostics, F1 Score (F1SC) is used to gauge the quality of outputs and outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Harmonic Mean of Precision and Recall, measured in score (points). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Software practice.

## Formula

```
F1SC = Harmonic Mean of Precision and Recall
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4058 (batch 9)
