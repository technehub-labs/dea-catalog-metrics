# dea:metric-assumed-breach-success-rate

Candidate Performance Metric record for **Assumed Breach Success Rate** (ABSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-assumed-breach-success-rate`
- **Name:** Assumed Breach Success Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ABSR

## 2. Definition

Assumed Breach Success Rate (ABSR) addresses exposure to adverse outcomes and is a fixture of threat intelligence & red team reporting. It is defined as Objectives Achieved by Red Team / Objectives; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how far assumed-breach exercises progress before defenders intervene. Starting inside the perimeter tests the controls that matter once the perimeter fails. Low success rates on easy objectives indicate defenders rely on perimeter luck. Read with red team detection rate and lateral movement detection coverage.

## Formula

```
Objectives Achieved by Red Team / Objectives
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3286 (batch 7)
