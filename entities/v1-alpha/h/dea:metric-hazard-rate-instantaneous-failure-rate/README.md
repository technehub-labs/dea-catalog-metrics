# dea:metric-hazard-rate-instantaneous-failure-rate

Candidate Performance Metric record for **Hazard Rate (Instantaneous Failure Rate)** (HRIFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hazard-rate-instantaneous-failure-rate`
- **Name:** Hazard Rate (Instantaneous Failure Rate)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HRIFR

## 2. Definition

A Reliability & Maintainability Engineering (Deep Dive) indicator, Hazard Rate (Instantaneous Failure Rate) (HRIFR) quantifies exposure to adverse outcomes. The formula is Failures in Interval / Surviving Units at Interval Start - reported in events per thousand or million (scaled). It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
HRIFR = Failures in Interval / Surviving Units at Interval Start
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** capability
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4096 (batch 9)
