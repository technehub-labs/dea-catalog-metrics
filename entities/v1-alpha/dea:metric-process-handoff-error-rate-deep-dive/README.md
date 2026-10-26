# dea:metric-process-handoff-error-rate-deep-dive

Candidate Performance Metric record for **Process Handoff Error Rate (Deep Dive)** (PHER-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-handoff-error-rate-deep-dive`
- **Name:** Process Handoff Error Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PHER-D

## 2. Definition

Within Balanced Scorecard - Internal Process Perspective, Process Handoff Error Rate (Deep Dive) (PHER-D) is used to gauge the quality of outputs and outcomes. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Errors at Process Handoffs / Handoffs, expressed in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Errors at Process Handoffs / Handoffs
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_internal_process_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3096 (batch 7)
