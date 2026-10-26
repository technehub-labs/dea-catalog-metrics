# dea:metric-ghost-vacancy-rate

Candidate Performance Metric record for **Ghost Vacancy Rate** (GVR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ghost-vacancy-rate`
- **Name:** Ghost Vacancy Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GVR

## 2. Definition

Ghost Vacancy Rate (GVR) captures exposure to adverse outcomes for organizations tracking workforce planning & analytics. It is computed as Approved Roles Unfilled beyond Target Time / Approved Roles, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures approved requisitions that are actually unstaffed but kept open. It matters because ghost vacancies misrepresent hiring capacity and absorb budget while producing nothing. Vacancies can be kept alive through minimal activity to preserve headcount claims. Read with Time to Fill and open requisition aging to confirm vacancy lists are real demand.

## Formula

```
Approved Roles Unfilled beyond Target Time / Approved Roles
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1458 (batch 5)
