# dea:metric-container-image-scan-gate-pass-rate

Candidate Performance Metric record for **Container Image Scan Gate Pass Rate** (CISGPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-container-image-scan-gate-pass-rate`
- **Name:** Container Image Scan Gate Pass Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CISGPR

## 2. Definition

Container Image Scan Gate Pass Rate (CISGPR) addresses conformance to standards, plans, or obligations and is a fixture of devsecops & application security engineering reporting. Its calculation is Images Passing Scan Policy before Deployment / Images, measured in percent (%). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
CISGPR = Images Passing Scan Policy before Deployment / Images
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2753 (batch 7)
