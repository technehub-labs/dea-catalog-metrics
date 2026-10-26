# dea:metric-drift-detection-rate

Candidate Performance Metric record for **Drift Detection Rate** (DDR-CS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-drift-detection-rate`
- **Name:** Drift Detection Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DDR-CS

## 2. Definition

Drift Detection Rate (DDR-CS) measures exposure to adverse outcomes in the Cloud Security Posture Management domain. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Config Drift Events Detected before Change Window / Drift Events, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Config Drift Events Detected before Change Window / Drift Events
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3312 (batch 7)
