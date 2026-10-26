# dea:metric-production-incident-root-cause-test-gap-ratio

Candidate Performance Metric record for **Production Incident Root Cause - Test Gap Ratio** (PIRC-TG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-production-incident-root-cause-test-gap-ratio`
- **Name:** Production Incident Root Cause - Test Gap Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PIRC-TG

## 2. Definition

A Software Testing & Quality Engineering indicator, Production Incident Root Cause - Test Gap Ratio (PIRC-TG) quantifies the quality of outputs and outcomes. It is defined as Incidents Attributed to Test Gaps / Incidents; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of production incidents whose root cause traces back to a gap in test coverage. It converts incidents into a direct audit of where the test suite is blind. Analysis quality depends on honest post-incident review, since causes are often multi-factor. Read with defect escape rate and post-incident review action closure rate.

## Formula

```
Incidents Attributed to Test Gaps / Incidents
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_testing_quality_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2719 (batch 7)
