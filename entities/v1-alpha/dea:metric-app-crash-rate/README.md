# dea:metric-app-crash-rate

Candidate Performance Metric record for **App Crash Rate** (ACR2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-app-crash-rate`
- **Name:** App Crash Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ACR2

## 2. Definition

App Crash Rate (ACR2) addresses the quality of outputs and outcomes and is a fixture of software engineering reporting. It is defined as Sessions with Crash / Total Sessions; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Sessions with Crash / Total Sessions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 299 (batch 1)
