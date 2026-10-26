# dea:metric-problem-recurrence-rate

Candidate Performance Metric record for **Problem Recurrence Rate** (PRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-problem-recurrence-rate`
- **Name:** Problem Recurrence Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PRR

## 2. Definition

Problem Recurrence Rate (PRR) captures the quality of outputs and outcomes for organizations tracking it service management. The formula is Recurring Incidents / Total Incidents - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how often incidents repeat after root-cause resolution. It matters because recurring problems show the fix never addressed the cause. Teams can hide recurrence by creating new incident categories for repeat symptoms. Read with Mean Time to Resolve and Change Success Rate to confirm fixes survive subsequent changes and time.

## Formula

```
Recurring Incidents / Total Incidents
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 304 (batch 1)
