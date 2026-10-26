# dea:metric-requisition-backlog-age

Candidate Performance Metric record for **Requisition Backlog Age** (RBA-TA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-requisition-backlog-age`
- **Name:** Requisition Backlog Age
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RBA-TA

## 2. Definition

A Talent Acquisition Deep Dive indicator, Requisition Backlog Age (RBA-TA) quantifies the utilization or availability of capacity. It is a working-level control: thresholds trigger immediate operational response. It is defined as Average Age of Unfilled Open Requisitions; the result is stated in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Average Age of Unfilled Open Requisitions
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** talent_acquisition_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3849 (batch 8)
