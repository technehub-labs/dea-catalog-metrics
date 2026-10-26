# dea:metric-close-process-exception-rate

Candidate Performance Metric record for **Close Process Exception Rate** (CPER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-close-process-exception-rate`
- **Name:** Close Process Exception Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPER

## 2. Definition

Within Internal Controls & Financial Reporting Integrity, Close Process Exception Rate (CPER) is used to gauge the quality of outputs and outcomes. It is computed as Close Tasks Requiring Rework / Close Tasks, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
CPER = Close Tasks Requiring Rework / Close Tasks
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3586 (batch 8)
