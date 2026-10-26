# dea:metric-build-success-rate

Candidate Performance Metric record for **Build Success Rate** (BSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-build-success-rate`
- **Name:** Build Success Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BSR

## 2. Definition

Build Success Rate (BSR) addresses the quality of outputs and outcomes and is a fixture of software engineering reporting. The formula is Successful Builds / Total Builds - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Successful Builds / Total Builds
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 289 (batch 1)
