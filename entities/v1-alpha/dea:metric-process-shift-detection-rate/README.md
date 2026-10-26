# dea:metric-process-shift-detection-rate

Candidate Performance Metric record for **Process Shift Detection Rate** (PSDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-shift-detection-rate`
- **Name:** Process Shift Detection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PSDR

## 2. Definition

A Process Capability & Six Sigma (Deep Dive) indicator, Process Shift Detection Rate (PSDR) quantifies the quality of outputs and outcomes. It is computed as Sustained Shifts Detected by Control Plan / Shifts Confirmed, expressed in percent (%). Its use is concentrated in Manufacturing. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
PSDR = Sustained Shifts Detected by Control Plan / Shifts Confirmed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4094 (batch 9)
