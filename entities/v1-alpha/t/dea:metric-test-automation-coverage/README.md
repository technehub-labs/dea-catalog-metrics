# dea:metric-test-automation-coverage

Candidate Performance Metric record for **Test Automation Coverage** (TAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-test-automation-coverage`
- **Name:** Test Automation Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TAC

## 2. Definition

A Software Engineering indicator, Test Automation Coverage (TAC) quantifies capability maturity or development. The formula is Automated Test Cases / Total Test Cases - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of code paths, requirements, or tests executed by automated suites. It matters because automation makes regression safety affordable at release cadence. Gaming risk includes trivial happy-path tests counted the same as critical-path coverage. Read with Change Success Rate and Defect Escape Rate to confirm coverage translates into real release safety.

## Formula

```
TAC = Automated Test Cases / Total Test Cases
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 293 (batch 1)
