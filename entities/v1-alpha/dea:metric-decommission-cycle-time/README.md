# dea:metric-decommission-cycle-time

Candidate Performance Metric record for **Decommission Cycle Time** (DCT-DC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-decommission-cycle-time`
- **Name:** Decommission Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DCT-DC

## 2. Definition

Decommission Cycle Time (DCT-DC) addresses how efficiently resources are converted into outputs and is a fixture of data centers & cloud infrastructure reporting. The formula is Days from Asset Retirement Request to Racked-Out - reported in days. It is a standard measure in the Technology sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Days from Asset Retirement Request to Racked-Out
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2148 (batch 6)
