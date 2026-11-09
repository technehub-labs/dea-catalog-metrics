# dea:metric-golden-image-compliance-rate

Candidate Performance Metric record for **Golden Image Compliance Rate** (GICR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-golden-image-compliance-rate`
- **Name:** Golden Image Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GICR

## 2. Definition

Golden Image Compliance Rate (GICR) addresses conformance to standards, plans, or obligations and is a fixture of cloud security posture management reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Workloads Launched from Approved Images / Workloads, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
GICR = Workloads Launched from Approved Images / Workloads
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3314 (batch 7)
