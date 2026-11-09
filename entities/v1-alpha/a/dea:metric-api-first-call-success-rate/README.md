# dea:metric-api-first-call-success-rate

Candidate Performance Metric record for **API First-Call Success Rate** (FCSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-first-call-success-rate`
- **Name:** API First-Call Success Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FCSR

## 2. Definition

A API Lifecycle Management indicator, API First-Call Success Rate (FCSR) quantifies the quality of outputs and outcomes. It is a working-level control: thresholds trigger immediate operational response. It is defined as Consumer Integrations Succeeding on First Attempt / Integrations; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
FCSR = Consumer Integrations Succeeding on First Attempt / Integrations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3211 (batch 7)
