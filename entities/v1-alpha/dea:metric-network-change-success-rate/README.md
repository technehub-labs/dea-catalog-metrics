# dea:metric-network-change-success-rate

Candidate Performance Metric record for **Network Change Success Rate** (NCSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-change-success-rate`
- **Name:** Network Change Success Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NCSR

## 2. Definition

Network Change Success Rate (NCSR) captures the quality of outputs and outcomes for organizations tracking network change & configuration management. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Changes Completed without Rollback or Incident / Changes - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Changes Completed without Rollback or Incident / Changes
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_change_configuration_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3360 (batch 7)
