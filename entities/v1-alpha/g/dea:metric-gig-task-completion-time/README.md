# dea:metric-gig-task-completion-time

Candidate Performance Metric record for **Gig Task Completion Time** (GTCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gig-task-completion-time`
- **Name:** Gig Task Completion Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GTCT

## 2. Definition

Gig Task Completion Time (GTCT) captures how efficiently resources are converted into outputs for organizations tracking gig & contingent workforce. Its calculation is Time from Acceptance to Task Completion, measured in hours. It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
GTCT = Time from Acceptance to Task Completion
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** gig_contingent_workforce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1461 (batch 5)
