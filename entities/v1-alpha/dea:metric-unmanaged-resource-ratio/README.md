# dea:metric-unmanaged-resource-ratio

Candidate Performance Metric record for **Unmanaged Resource Ratio** (URR-CS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unmanaged-resource-ratio`
- **Name:** Unmanaged Resource Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** URR-CS

## 2. Definition

Within Cloud Security Posture Management, Unmanaged Resource Ratio (URR-CS) is used to gauge governance. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Resources without Tagged Owner / Resources - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Resources without Tagged Owner / Resources
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** governance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3310 (batch 7)
