# dea:metric-process-z-score-short-term

Candidate Performance Metric record for **Process Z-Score (Short Term)** (PZST) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-z-score-short-term`
- **Name:** Process Z-Score (Short Term)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PZST

## 2. Definition

Process Z-Score (Short Term) (PZST) captures the quality of outputs and outcomes for organizations tracking process capability & six sigma (deep dive). The formula is Sigma Distance of Mean to Nearest Spec Limit - reported in score (points). It is a standard measure in the Manufacturing sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Sigma Distance of Mean to Nearest Spec Limit
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4086 (batch 9)
