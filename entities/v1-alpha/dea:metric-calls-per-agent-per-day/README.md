# dea:metric-calls-per-agent-per-day

Candidate Performance Metric record for **Calls per Agent per Day** (CPAD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-calls-per-agent-per-day`
- **Name:** Calls per Agent per Day
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPAD

## 2. Definition

A Contact Center indicator, Calls per Agent per Day (CPAD) quantifies the utilization or availability of capacity. It is defined as Calls Handled / Agent Days Worked; the result is stated in ratio (x:1 or x). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Calls Handled / Agent Days Worked
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 568 (batch 2)
