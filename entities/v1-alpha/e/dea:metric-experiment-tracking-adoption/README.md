# dea:metric-experiment-tracking-adoption

Candidate Performance Metric record for **Experiment Tracking Adoption** (ETA-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-experiment-tracking-adoption`
- **Name:** Experiment Tracking Adoption
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ETA-M

## 2. Definition

Experiment Tracking Adoption (ETA-M) captures the quality of outputs and outcomes for organizations tracking mlops & model lifecycle operations. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Experiments Logged in Tracking System / Experiments, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ETA-M = Experiments Logged in Tracking System / Experiments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2529 (batch 7)
