# dea:metric-call-drop-rate

Candidate Performance Metric record for **Call Drop Rate** (CDR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-call-drop-rate`
- **Name:** Call Drop Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CDR-T

## 2. Definition

Call Drop Rate (CDR-T) measures the quality of outputs and outcomes in the Telecommunications domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Dropped Calls / Total Calls - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Telecommunications sector.

## Formula

```
Dropped Calls / Total Calls
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
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 527 (batch 1)
