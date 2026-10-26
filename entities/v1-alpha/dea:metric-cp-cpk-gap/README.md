# dea:metric-cp-cpk-gap

Candidate Performance Metric record for **Cp-Cpk Gap** (CCGAP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cp-cpk-gap`
- **Name:** Cp-Cpk Gap
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCGAP

## 2. Definition

Cp-Cpk Gap (CCGAP) measures the quality of outputs and outcomes in the Process Capability & Six Sigma (Deep Dive) domain. It is defined as Cp minus Cpk (Centering Penalty); the result is stated in ratio (x:1 or x). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Manufacturing, it is a recognized element of the standard performance toolkit.

## Formula

```
Cp minus Cpk (Centering Penalty)
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4085 (batch 9)
