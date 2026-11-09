# dea:metric-duplicate-code-rate-deep-dive

Candidate Performance Metric record for **Duplicate Code Rate (Deep Dive)** (DCRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-duplicate-code-rate-deep-dive`
- **Name:** Duplicate Code Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCRD

## 2. Definition

Duplicate Code Rate (Deep Dive) (DCRD) addresses the quality of outputs and outcomes and is a fixture of code quality & static analysis reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Duplicated Lines / Total Lines - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Software sector.

## Formula

```
DCRD = Duplicated Lines / Total Lines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4179 (batch 9)
