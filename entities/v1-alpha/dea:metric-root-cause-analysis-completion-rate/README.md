# dea:metric-root-cause-analysis-completion-rate

Candidate Performance Metric record for **Root Cause Analysis Completion Rate** (RCACR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-root-cause-analysis-completion-rate`
- **Name:** Root Cause Analysis Completion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RCACR

## 2. Definition

A IT Incident & Major Problem Management indicator, Root Cause Analysis Completion Rate (RCACR) quantifies conformance to standards, plans, or obligations. Its calculation is RCAs Completed within Target for Major Incidents / Major Incidents, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of qualifying incidents with completed, quality-reviewed RCA. RCA converts outages into durable fixes. Blame-driven cultures produce shallow RCAs that name people, not causes. Read with post-incident review action closure rate and incident caused by change rate.

## Formula

```
RCAs Completed within Target for Major Incidents / Major Incidents
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2891 (batch 7)
