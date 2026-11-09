# dea:metric-shadow-cloud-asset-detection-rate

Candidate Performance Metric record for **Shadow Cloud Asset Detection Rate** (SCADR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shadow-cloud-asset-detection-rate`
- **Name:** Shadow Cloud Asset Detection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCADR

## 2. Definition

Shadow Cloud Asset Detection Rate (SCADR) measures exposure to adverse outcomes in the Cloud Security Posture Management domain. It is computed as Unregistered Assets Discovered per Discovery Run, expressed in count (items per period). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
SCADR = Unregistered Assets Discovered per Discovery Run
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3315 (batch 7)
