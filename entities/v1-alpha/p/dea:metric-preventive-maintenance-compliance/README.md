# dea:metric-preventive-maintenance-compliance

Candidate Performance Metric record for **Preventive Maintenance Compliance** (PMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-preventive-maintenance-compliance`
- **Name:** Preventive Maintenance Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PMC

## 2. Definition

A Maintenance & Reliability indicator, Preventive Maintenance Compliance (PMC) quantifies conformance to standards, plans, or obligations. It is defined as PM Tasks Completed on Time / PM Tasks Scheduled; the result is stated in percent (%). In Manufacturing, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of scheduled preventive maintenance completed on time. It matters because PM deferral is the classic trade of today's uptime for tomorrow's breakdowns. It can be gamed by marking PM complete with partial work or closing work orders administratively. Read with Availability and Emergency Work Order Rate to confirm PM discipline converts into reliability.

## Formula

```
PMC = PM Tasks Completed on Time / PM Tasks Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 266 (batch 1)
