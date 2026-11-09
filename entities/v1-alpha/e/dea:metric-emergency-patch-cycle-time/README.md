# dea:metric-emergency-patch-cycle-time

Candidate Performance Metric record for **Emergency Patch Cycle Time** (EPCT-VM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-patch-cycle-time`
- **Name:** Emergency Patch Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EPCT-VM

## 2. Definition

Emergency Patch Cycle Time (EPCT-VM) measures how efficiently resources are converted into outputs in the Vulnerability & Exposure Management domain. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Hours from Emergency Patch Release to Deployment, expressed in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
EPCT-VM = Hours from Emergency Patch Release to Deployment
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2805 (batch 7)
