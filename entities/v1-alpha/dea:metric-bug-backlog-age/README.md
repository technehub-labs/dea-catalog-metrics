# dea:metric-bug-backlog-age

Candidate Performance Metric record for **Bug Backlog Age** (BBA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bug-backlog-age`
- **Name:** Bug Backlog Age
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BBA

## 2. Definition

Bug Backlog Age (BBA) captures exposure to adverse outcomes for organizations tracking software engineering. It is defined as Median Age of Open Defects; the result is stated in days. It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Median Age of Open Defects
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 287 (batch 1)
