# dea:metric-critical-alert-queue-time-95th-percentile

Candidate Performance Metric record for **Critical Alert Queue Time - 95th Percentile** (CAQT95) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-critical-alert-queue-time-95th-percentile`
- **Name:** Critical Alert Queue Time - 95th Percentile
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAQT95

## 2. Definition

Critical Alert Queue Time - 95th Percentile (CAQT95) captures the utilization or availability of capacity for organizations tracking secops & security operations center. The formula is Minutes Critical Alerts Wait in Queue - reported in minutes. It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
CAQT95 = Minutes Critical Alerts Wait in Queue
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2794 (batch 7)
