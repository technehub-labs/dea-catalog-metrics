# dea:metric-pipeline-stage-failure-attribution-rate

Candidate Performance Metric record for **Pipeline Stage Failure Attribution Rate** (PSFAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pipeline-stage-failure-attribution-rate`
- **Name:** Pipeline Stage Failure Attribution Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PSFAR

## 2. Definition

Pipeline Stage Failure Attribution Rate (PSFAR) captures the quality of outputs and outcomes for organizations tracking continuous integration. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Failures with Root Cause Attributed / Failures - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Failures with Root Cause Attributed / Failures
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2673 (batch 7)
