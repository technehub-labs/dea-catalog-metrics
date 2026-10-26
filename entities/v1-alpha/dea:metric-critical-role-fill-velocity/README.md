# dea:metric-critical-role-fill-velocity

Candidate Performance Metric record for **Critical Role Fill Velocity** (CRFV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-critical-role-fill-velocity`
- **Name:** Critical Role Fill Velocity
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CRFV

## 2. Definition

Critical Role Fill Velocity (CRFV) addresses how efficiently resources are converted into outputs and is a fixture of workforce planning & analytics reporting. Its calculation is Days to Fill Critical Role from Approval, measured in days. It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how quickly openings in business-critical roles are filled with qualified candidates, from requisition to productive start. Slow fills in critical roles are a direct strategic tax: strategy waits on staffing. Velocity gains from lowering the bar are false wins, so pair with quality measures like early performance and regretted attrition in those roles. Read with staffing gap ratio and successor readiness ratio.

## Formula

```
Days to Fill Critical Role from Approval
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1453 (batch 5)
