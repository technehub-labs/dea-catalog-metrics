# dea:metric-escape-rate

Candidate Performance Metric record for **Escape Rate** (ER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-escape-rate`
- **Name:** Escape Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ER

## 2. Definition

Within Quality Management, Escape Rate (ER) is used to gauge the quality of outputs and outcomes. The formula is Defects Found Downstream / Defects Present at Stage - reported in percent (%). It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Defects Found Downstream / Defects Present at Stage
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 243 (batch 1)
