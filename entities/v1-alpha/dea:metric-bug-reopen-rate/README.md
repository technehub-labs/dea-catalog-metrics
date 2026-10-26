# dea:metric-bug-reopen-rate

Candidate Performance Metric record for **Bug Reopen Rate** (BRR-QA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bug-reopen-rate`
- **Name:** Bug Reopen Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BRR-QA

## 2. Definition

Bug Reopen Rate (BRR-QA) measures the quality of outputs and outcomes in the Software Testing & Quality Engineering domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Reopened Bugs / Closed Bugs - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Reopened Bugs / Closed Bugs
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_testing_quality_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2714 (batch 7)
