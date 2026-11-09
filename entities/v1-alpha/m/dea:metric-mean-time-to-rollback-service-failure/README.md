# dea:metric-mean-time-to-rollback-service-failure

Candidate Performance Metric record for **Mean Time to Rollback - Service Failure** (MTRS-SF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-rollback-service-failure`
- **Name:** Mean Time to Rollback - Service Failure
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTRS-SF

## 2. Definition

A Observability & Site Reliability Engineering indicator, Mean Time to Rollback - Service Failure (MTRS-SF) quantifies how efficiently resources are converted into outputs. Its calculation is Minutes from Detected Failure to Rollback Complete, measured in minutes. It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
MTRS-SF = Minutes from Detected Failure to Rollback Complete
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2874 (batch 7)
