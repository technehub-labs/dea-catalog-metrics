# dea:metric-burnout-index

Candidate Performance Metric record for **Burnout Index** (BOI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-burnout-index`
- **Name:** Burnout Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BOI

## 2. Definition

A Employee Wellbeing indicator, Burnout Index (BOI) quantifies exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Weighted Index of Exhaustion, Cynicism, and Efficacy Survey Items, measured in index (0-100 or normalized). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The burnout index measures exhaustion, cynicism, and reduced professional efficacy - the Maslach-model three dimensions that define burnout rather than simple stress - and it is the leading-indicator metric of workforce sustainability: burnout predicts absence, turnover, errors, and disengagement before any of them show in operational numbers. Its measurement honesty requires validated instruments (Maslach Burnout Inventory and peers) rather than single ad-hoc questions, and the response-confidentiality question is real: honest burnout reporting requires genuine anonymity, and reported index trends are hostage to perceived safety. The root-cause structure is workload-and-control shaped: burnout follows chronic workload pressure plus low autonomy and low recovery, so the index is a job-design signal more than an individual one. Read with workload and staffing metrics (the structural drivers), turnover and absence trends as the lagging validations, and unit-level distribution rather than company average.

## Formula

```
Weighted Index of Exhaustion, Cynicism, and Efficacy Survey Items
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** employee_wellbeing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1230 (batch 4)
