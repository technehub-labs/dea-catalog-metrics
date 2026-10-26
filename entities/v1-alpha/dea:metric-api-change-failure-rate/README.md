# dea:metric-api-change-failure-rate

Candidate Performance Metric record for **API Change Failure Rate** (APICFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-change-failure-rate`
- **Name:** API Change Failure Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APICFR

## 2. Definition

API Change Failure Rate (APICFR) captures the quality of outputs and outcomes for organizations tracking api lifecycle management. It is defined as API Changes Causing Incident / API Changes; the result is stated in percent (%). In Software, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
API Changes Causing Incident / API Changes
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3224 (batch 7)
