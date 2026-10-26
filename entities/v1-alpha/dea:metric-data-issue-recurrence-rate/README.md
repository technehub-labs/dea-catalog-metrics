# dea:metric-data-issue-recurrence-rate

Candidate Performance Metric record for **Data Issue Recurrence Rate** (DIRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-issue-recurrence-rate`
- **Name:** Data Issue Recurrence Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DIRR

## 2. Definition

Data Issue Recurrence Rate (DIRR) measures the quality of outputs and outcomes in the Data Governance & Stewardship domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Issues Reopened after Closure / Closed Issues - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Issues Reopened after Closure / Closed Issues
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_governance_stewardship

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3606 (batch 8)
