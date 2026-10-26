# dea:metric-public-exposure-rate-cloud-assets

Candidate Performance Metric record for **Public Exposure Rate (Cloud Assets)** (PERC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-public-exposure-rate-cloud-assets`
- **Name:** Public Exposure Rate (Cloud Assets)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PERC

## 2. Definition

Within Cloud Security Posture Management, Public Exposure Rate (Cloud Assets) (PERC) is used to gauge exposure to adverse outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Assets Publicly Exposed / Cloud Assets, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Assets Publicly Exposed / Cloud Assets
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3305 (batch 7)
