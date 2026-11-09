# dea:metric-retention-schedule-compliance-rate

Candidate Performance Metric record for **Retention Schedule Compliance Rate** (RSCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-retention-schedule-compliance-rate`
- **Name:** Retention Schedule Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RSCR

## 2. Definition

A Records & Information Management indicator, Retention Schedule Compliance Rate (RSCR) quantifies conformance to standards, plans, or obligations. It is computed as Records Disposed or Held per Schedule / Records Sampled, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
RSCR = Records Disposed or Held per Schedule / Records Sampled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** records_information_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3676 (batch 8)
