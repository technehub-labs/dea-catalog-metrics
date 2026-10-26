# dea:metric-business-downtime-per-crisis-event

Candidate Performance Metric record for **Business Downtime per Crisis Event** (BDCE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-business-downtime-per-crisis-event`
- **Name:** Business Downtime per Crisis Event
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BDCE

## 2. Definition

A Crisis Management & Emergency Response indicator, Business Downtime per Crisis Event (BDCE) quantifies exposure to adverse outcomes. Its calculation is Average Operating Hours Lost per Crisis, measured in hours. It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the operational downtime attributable to each crisis. It converts crisis management performance into P&L language. Downtime definitions that exclude degraded-but-operating states understate impact. Read with maximum tolerable downtime headroom and business impact quantification.

## Formula

```
Average Operating Hours Lost per Crisis
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** crisis_management_emergency_response

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3548 (batch 8)
