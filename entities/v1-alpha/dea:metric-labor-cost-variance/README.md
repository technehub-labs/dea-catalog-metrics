# dea:metric-labor-cost-variance

Candidate Performance Metric record for **Labor Cost Variance** (LCV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-labor-cost-variance`
- **Name:** Labor Cost Variance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LCV

## 2. Definition

Within Workforce Planning & Analytics, Labor Cost Variance (LCV) is used to gauge conformance to standards, plans, or obligations. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as (Actual Labor Cost - Planned Labor Cost) / Planned Labor Cost; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures deviation of actual labor cost from the staffing plan. It matters because labor is the largest controllable cost in most service businesses. Variance can be managed by booking overtime under contractor spend. Read with Overtime Hours and Contract Labor reliance to confirm variance control is honest.

## Formula

```
(Actual Labor Cost - Planned Labor Cost) / Planned Labor Cost
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1454 (batch 5)
