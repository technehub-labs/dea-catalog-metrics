# dea:metric-asset-failure-recurrence-rate

Candidate Performance Metric record for **Asset Failure Recurrence Rate** (AFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-failure-recurrence-rate`
- **Name:** Asset Failure Recurrence Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AFR

## 2. Definition

Within Maintenance & Reliability, Asset Failure Recurrence Rate (AFR) is used to gauge the quality of outputs and outcomes. It is computed as Repeat Failures within Warranty of Repair / Total Failures, expressed in percent (%). Its use is concentrated in Manufacturing. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how often the same asset fails again after a repair. It matters because repeat failures expose root-cause neglect and wasted maintenance spend. It can be gamed by treating each recurrence as a new failure type or replacing the asset ID to reset the history. Read with Mean Time Between Failures and Corrective Action Effectiveness to confirm repairs address causes, not symptoms.

## Formula

```
Repeat Failures within Warranty of Repair / Total Failures
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 276 (batch 1)
