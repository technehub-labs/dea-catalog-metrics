# dea:metric-installation-rework-rate-telecom

Candidate Performance Metric record for **Installation Rework Rate (Telecom)** (IRRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-installation-rework-rate-telecom`
- **Name:** Installation Rework Rate (Telecom)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IRRT

## 2. Definition

Installation Rework Rate (Telecom) (IRRT) addresses the quality of outputs and outcomes and is a fixture of telecom field & installation reporting. It is defined as Jobs Requiring Return Visit / Jobs Completed; the result is stated in percent (%). In Telecommunications, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
IRRT = Jobs Requiring Return Visit / Jobs Completed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** telecom_field_installation
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1281 (batch 5)
