# dea:metric-test-automation-coverage-deep-dive

Candidate Performance Metric record for **Test Automation Coverage (Deep Dive)** (TAC-QA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-test-automation-coverage-deep-dive`
- **Name:** Test Automation Coverage (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TAC-QA

## 2. Definition

A Software Testing & Quality Engineering indicator, Test Automation Coverage (Deep Dive) (TAC-QA) quantifies capability maturity or development. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Automated Test Cases / Total Test Cases; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of defined test cases executed by automated suites rather than manual effort. Automation is what makes frequent, safe releases economically possible; manual regression cycles cap delivery velocity. Coverage counted against an outdated or shallow test design inflates the number without reducing risk. Read with defect escape rate and mutation testing kill score.

## Formula

```
TAC-QA = Automated Test Cases / Total Test Cases
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_testing_quality_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2705 (batch 7)
