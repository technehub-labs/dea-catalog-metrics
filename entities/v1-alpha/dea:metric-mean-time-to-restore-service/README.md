# dea:metric-mean-time-to-restore-service

Candidate Performance Metric record for **Mean Time to Restore Service** (MTTRS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-restore-service`
- **Name:** Mean Time to Restore Service
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTTRS

## 2. Definition

A Software Engineering indicator, Mean Time to Restore Service (MTTRS) quantifies the quality of outputs and outcomes. It is computed as Median Time from Incident Start to Service Restoration, expressed in hours. It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

MTTRS, the fourth DORA metric, measures elapsed time from incident start (or detection) to service restored for users - usually as a median, so rare catastrophic outages do not distort it. It captures operational resilience rather than delivery speed: elite performers restore in under an hour, laggards take days. Two subtleties: use restore, not resolve, because users care about service, not root cause; and pair it with change failure rate - restoring fast while breaking things often is quick firefighting, not improvement.

## Formula

```
Median Time from Incident Start to Service Restoration
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** DORA research program (DevOps Research and Assessment)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 280 (batch 1)
