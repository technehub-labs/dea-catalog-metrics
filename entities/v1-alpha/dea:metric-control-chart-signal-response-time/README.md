# dea:metric-control-chart-signal-response-time

Candidate Performance Metric record for **Control Chart Signal Response Time** (CCSRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-control-chart-signal-response-time`
- **Name:** Control Chart Signal Response Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCSRT

## 2. Definition

Within Process Capability & Six Sigma (Deep Dive), Control Chart Signal Response Time (CCSRT) is used to gauge how efficiently resources are converted into outputs. Its calculation is Hours from Control Chart Signal to Containment Action, measured in hours. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Manufacturing practice.

## Formula

```
Hours from Control Chart Signal to Containment Action
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** capability
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4093 (batch 9)
