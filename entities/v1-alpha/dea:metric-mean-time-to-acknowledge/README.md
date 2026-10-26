# dea:metric-mean-time-to-acknowledge

Candidate Performance Metric record for **Mean Time to Acknowledge** (MTTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-acknowledge`
- **Name:** Mean Time to Acknowledge
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTTA

## 2. Definition

Mean Time to Acknowledge (MTTA) captures how efficiently resources are converted into outputs for organizations tracking it service management. The formula is Total Acknowledgment Time / Incidents - reported in minutes. It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Total Acknowledgment Time / Incidents
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 302 (batch 1)
