# dea:metric-s-op-meeting-cadence-compliance

Candidate Performance Metric record for **S&OP Meeting Cadence Compliance** (SMCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-s-op-meeting-cadence-compliance`
- **Name:** S&OP Meeting Cadence Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SMCC

## 2. Definition

A Sales & Operations Planning indicator, S&OP Meeting Cadence Compliance (SMCC) quantifies conformance to standards, plans, or obligations. The formula is S&OP Cycles Completed per Standard / Cycles Due - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether the monthly sales and operations planning cycle actually happens on schedule with the required decision-makers present. It sounds procedural, but S&OP value comes almost entirely from the disciplined cadence: skipped or degraded meetings cascade into forecast distrust and expediting cost. Honest reads check decision quality, not attendance - a fully attended meeting that defers every mismatch is non-compliance in spirit. Read with consensus forecast accuracy (S&OP) and excess and obsolete inventory ratio.

## Formula

```
S&OP Cycles Completed per Standard / Cycles Due
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1288 (batch 5)
