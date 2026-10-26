# dea:metric-handoff-count-per-process

Candidate Performance Metric record for **Handoff Count per Process** (HCPP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-handoff-count-per-process`
- **Name:** Handoff Count per Process
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** HCPP

## 2. Definition

A Operating Model & Process Health Deep Dive indicator, Handoff Count per Process (HCPP) quantifies how efficiently resources are converted into outputs. The formula is Average Handoffs between Functions per Process Run - reported in count (items per period). It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Average Handoffs between Functions per Process Run
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operating_model_process_health_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3498 (batch 7)
