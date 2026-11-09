# dea:metric-runbook-coverage-services

Candidate Performance Metric record for **Runbook Coverage (Services)** (RBCS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-runbook-coverage-services`
- **Name:** Runbook Coverage (Services)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RBCS

## 2. Definition

Runbook Coverage (Services) (RBCS) addresses capability maturity or development and is a fixture of sre & observability standard measures reporting. The formula is Critical Alerts with Runbook / Critical Alert Types - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Software sector.

## Formula

```
RBCS = Critical Alerts with Runbook / Critical Alert Types
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4386 (batch 11)
