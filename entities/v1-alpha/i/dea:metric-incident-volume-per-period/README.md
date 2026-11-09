# dea:metric-incident-volume-per-period

Candidate Performance Metric record for **Incident Volume per Period** (IVPP-IT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-volume-per-period`
- **Name:** Incident Volume per Period
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IVPP-IT

## 2. Definition

Within IT Incident & Major Problem Management, Incident Volume per Period (IVPP-IT) is used to gauge exposure to adverse outcomes. It is defined as Incidents Logged per Month; the result is stated in count (items per period). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the count of incidents recorded per period. It is the ambient noise floor of operational health. Rising volume with flat staffing predicts SLA collapse; falling volume can mean reporting fatigue rather than improvement. Read with recurring incident ratio and incident detection via monitoring ratio.

## Formula

```
IVPP-IT = Incidents Logged per Month
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2883 (batch 7)
