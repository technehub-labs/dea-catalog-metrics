# dea:metric-out-of-spec-rate

Candidate Performance Metric record for **Out-of-Spec Rate** (OSPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-out-of-spec-rate`
- **Name:** Out-of-Spec Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OSPR

## 2. Definition

Out-of-Spec Rate (OSPR) measures the quality of outputs and outcomes in the Process Capability & Six Sigma (Deep Dive) domain. It is computed as Units Outside Specification / Units Produced, expressed in percent (%). Its use is concentrated in Manufacturing. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Units Outside Specification / Units Produced
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4088 (batch 9)
