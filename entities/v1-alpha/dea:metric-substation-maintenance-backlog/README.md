# dea:metric-substation-maintenance-backlog

Candidate Performance Metric record for **Substation Maintenance Backlog** (SMB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-substation-maintenance-backlog`
- **Name:** Substation Maintenance Backlog
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SMB

## 2. Definition

Substation Maintenance Backlog (SMB) addresses exposure to adverse outcomes and is a fixture of utilities field operations & grid reporting. It is defined as Overdue Maintenance Tasks / Total Tasks; the result is stated in percent (%). In Utilities, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Overdue Maintenance Tasks / Total Tasks
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1892 (batch 6)
