# dea:metric-out-of-window-change-detection-rate

Candidate Performance Metric record for **Out-of-Window Change Detection Rate** (OWCDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-out-of-window-change-detection-rate`
- **Name:** Out-of-Window Change Detection Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OWCDR

## 2. Definition

Out-of-Window Change Detection Rate (OWCDR) addresses conformance to standards, plans, or obligations and is a fixture of network change & configuration management reporting. It is computed as Unauthorized Changes Detected / Total Changes Audited, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Unauthorized Changes Detected / Total Changes Audited
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_change_configuration_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3377 (batch 7)
