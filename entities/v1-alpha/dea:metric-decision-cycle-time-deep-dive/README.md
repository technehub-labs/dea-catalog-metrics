# dea:metric-decision-cycle-time-deep-dive

Candidate Performance Metric record for **Decision Cycle Time (Deep Dive)** (DCTDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-decision-cycle-time-deep-dive`
- **Name:** Decision Cycle Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCTDD

## 2. Definition

Decision Cycle Time (Deep Dive) (DCTDD) addresses how efficiently resources are converted into outputs and is a fixture of operating model & process health deep dive reporting. It is defined as Days from Decision Request to Decision Made; the result is stated in days. It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures elapsed time from decision need to decision made, across decision classes. Cycle time is the pulse of organizational agility. Back-dating the decision need shortens the metric dishonestly. Read with decision cycle time - strategic decisions and governance layer efficiency ratio.

## Formula

```
DCTDD = Days from Decision Request to Decision Made
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** transformation
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operating_model_process_health_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3509 (batch 7)
