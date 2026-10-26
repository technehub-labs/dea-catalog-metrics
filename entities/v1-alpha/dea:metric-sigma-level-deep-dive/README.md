# dea:metric-sigma-level-deep-dive

Candidate Performance Metric record for **Sigma Level (Deep Dive)** (SIGDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sigma-level-deep-dive`
- **Name:** Sigma Level (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SIGDD

## 2. Definition

A Process Capability & Six Sigma (Deep Dive) indicator, Sigma Level (Deep Dive) (SIGDD) quantifies the quality of outputs and outcomes. It is computed as Defects per Million Opportunities converted to Sigma Scale, expressed in score (points). Its use is concentrated in Manufacturing. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures process performance in defects per million opportunities, expressed in standard deviations. Sigma is the common language of process capability across functions. Definitions of an opportunity set generously inflate the level. Read with process capability index (Cp/Cpk) and process first-pass yield trend (Deep Dive).

## Formula

```
Defects per Million Opportunities converted to Sigma Scale
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4079 (batch 9)
