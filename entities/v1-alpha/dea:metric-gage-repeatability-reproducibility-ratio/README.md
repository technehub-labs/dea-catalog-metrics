# dea:metric-gage-repeatability-reproducibility-ratio

Candidate Performance Metric record for **Gage Repeatability & Reproducibility Ratio** (GRNR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gage-repeatability-reproducibility-ratio`
- **Name:** Gage Repeatability & Reproducibility Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GRNR

## 2. Definition

Gage Repeatability & Reproducibility Ratio (GRNR) captures the quality of outputs and outcomes for organizations tracking process capability & six sigma (deep dive). It is computed as Measurement System Variation / Total Variation, expressed in percent (%). Its use is concentrated in Manufacturing. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Measurement System Variation / Total Variation
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4089 (batch 9)
