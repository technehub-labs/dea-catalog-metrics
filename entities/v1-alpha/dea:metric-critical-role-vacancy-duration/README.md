# dea:metric-critical-role-vacancy-duration

Candidate Performance Metric record for **Critical Role Vacancy Duration** (CRVD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-critical-role-vacancy-duration`
- **Name:** Critical Role Vacancy Duration
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRVD

## 2. Definition

Critical Role Vacancy Duration (CRVD) measures exposure to adverse outcomes in the Workforce Planning & Productivity domain. It is computed as Days Critical Roles Remain Vacant, expressed in days. It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how long business-critical roles remain unfilled. Every open critical role is delayed strategy and redistributed load. Duration measured from job posting rather than approval start understates. Read with time-to-fill (critical roles) and niche role search success rate.

## Formula

```
CRVD = Days Critical Roles Remain Vacant
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_productivity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3903 (batch 8)
