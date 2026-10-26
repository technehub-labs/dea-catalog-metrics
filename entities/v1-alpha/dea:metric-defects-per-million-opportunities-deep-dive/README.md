# dea:metric-defects-per-million-opportunities-deep-dive

Candidate Performance Metric record for **Defects per Million Opportunities (Deep Dive)** (DPMOD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-defects-per-million-opportunities-deep-dive`
- **Name:** Defects per Million Opportunities (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DPMOD

## 2. Definition

A Process Capability & Six Sigma (Deep Dive) indicator, Defects per Million Opportunities (Deep Dive) (DPMOD) quantifies the quality of outputs and outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Defects / (Units x Opportunities) x 1,000,000, measured in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Manufacturing practice.

## Formula

```
Defects / (Units x Opportunities) x 1,000,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4080 (batch 9)
