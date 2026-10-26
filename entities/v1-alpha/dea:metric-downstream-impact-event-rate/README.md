# dea:metric-downstream-impact-event-rate

Candidate Performance Metric record for **Downstream Impact Event Rate** (DIER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-downstream-impact-event-rate`
- **Name:** Downstream Impact Event Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DIER

## 2. Definition

Within Data Quality Management, Downstream Impact Event Rate (DIER) is used to gauge exposure to adverse outcomes. It is computed as Quality Failures Reaching Downstream Consumers / Failures, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Quality Failures Reaching Downstream Consumers / Failures
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3629 (batch 8)
