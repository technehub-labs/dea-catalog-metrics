# dea:metric-secret-scanning-gate-pass-rate

Candidate Performance Metric record for **Secret Scanning Gate Pass Rate** (SSGPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-secret-scanning-gate-pass-rate`
- **Name:** Secret Scanning Gate Pass Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SSGPR

## 2. Definition

Secret Scanning Gate Pass Rate (SSGPR) addresses exposure to adverse outcomes and is a fixture of continuous integration reporting. Its calculation is Builds Passing Secret Scan Gate / Builds, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Builds Passing Secret Scan Gate / Builds
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2677 (batch 7)
