# dea:metric-measurement-system-bias

Candidate Performance Metric record for **Measurement System Bias** (MSB-SS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-measurement-system-bias`
- **Name:** Measurement System Bias
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MSB-SS

## 2. Definition

Measurement System Bias (MSB-SS) addresses the quality of outputs and outcomes and is a fixture of process capability & six sigma (deep dive) reporting. It is computed as Average Measurement Deviation from Reference Standard, expressed in percent (%). Its use is concentrated in Manufacturing. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
MSB-SS = Average Measurement Deviation from Reference Standard
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4090 (batch 9)
