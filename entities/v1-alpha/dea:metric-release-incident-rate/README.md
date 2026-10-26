# dea:metric-release-incident-rate

Candidate Performance Metric record for **Release Incident Rate** (RIR-RM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-release-incident-rate`
- **Name:** Release Incident Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RIR-RM

## 2. Definition

A Release Management & Environments indicator, Release Incident Rate (RIR-RM) quantifies exposure to adverse outcomes. Its calculation is Incidents per Release, measured in count (items per period). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the frequency of production incidents attributable to releases. It is the safety score of the delivery pipeline. Teams can game it by reclassifying release fallout as unrelated issues. Read with change failure rate and incident caused by change rate.

## Formula

```
Incidents per Release
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
- **Domain:** release_management_environments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2742 (batch 7)
