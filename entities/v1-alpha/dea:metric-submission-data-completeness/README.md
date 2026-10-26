# dea:metric-submission-data-completeness

Candidate Performance Metric record for **Submission Data Completeness** (SDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-submission-data-completeness`
- **Name:** Submission Data Completeness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SDC

## 2. Definition

Submission Data Completeness (SDC) addresses the quality of outputs and outcomes and is a fixture of insurance underwriting reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Complete Submissions / Submissions Received, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Insurance.

## Formula

```
SDC = Complete Submissions / Submissions Received
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1515 (batch 6)
