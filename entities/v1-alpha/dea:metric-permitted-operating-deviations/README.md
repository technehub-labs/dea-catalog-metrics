# dea:metric-permitted-operating-deviations

Candidate Performance Metric record for **Permitted Operating Deviations** (POD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-permitted-operating-deviations`
- **Name:** Permitted Operating Deviations
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** POD

## 2. Definition

A Regulatory Affairs & Compliance Operations indicator, Permitted Operating Deviations (POD) quantifies exposure to adverse outcomes. Its calculation is Approved Deviations from Regulatory Standard / Requests, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
POD = Approved Deviations from Regulatory Standard / Requests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** regulatory_affairs_compliance_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1596 (batch 6)
