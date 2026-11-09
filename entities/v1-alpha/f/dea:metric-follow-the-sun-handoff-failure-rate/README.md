# dea:metric-follow-the-sun-handoff-failure-rate

Candidate Performance Metric record for **Follow-the-Sun Handoff Failure Rate** (FTSHFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-follow-the-sun-handoff-failure-rate`
- **Name:** Follow-the-Sun Handoff Failure Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FTSHFR

## 2. Definition

Within Network Operations Center (Deep Dive), Follow-the-Sun Handoff Failure Rate (FTSHFR) is used to gauge the quality of outputs and outcomes. It is computed as Handoffs with Dropped Context / Handoffs, expressed in events per thousand or million (scaled). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
FTSHFR = Handoffs with Dropped Context / Handoffs
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2859 (batch 7)
