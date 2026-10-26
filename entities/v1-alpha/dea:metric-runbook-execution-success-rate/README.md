# dea:metric-runbook-execution-success-rate

Candidate Performance Metric record for **Runbook Execution Success Rate** (RESR-NOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-runbook-execution-success-rate`
- **Name:** Runbook Execution Success Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RESR-NOC

## 2. Definition

Runbook Execution Success Rate (RESR-NOC) addresses the quality of outputs and outcomes and is a fixture of network operations center (deep dive) reporting. Its calculation is Runbook-Guided Resolutions Successful / Executed, measured in percent (%). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
RESR-NOC = Runbook-Guided Resolutions Successful / Executed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2851 (batch 7)
