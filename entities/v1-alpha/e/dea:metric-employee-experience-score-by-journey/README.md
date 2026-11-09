# dea:metric-employee-experience-score-by-journey

Candidate Performance Metric record for **Employee Experience Score by Journey** (EXJB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-employee-experience-score-by-journey`
- **Name:** Employee Experience Score by Journey
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EXJB

## 2. Definition

Employee Experience Score by Journey (EXJB) addresses the engagement or satisfaction of the people involved and is a fixture of culture & employee experience reporting. Its calculation is Average Satisfaction across Key Employee Journey Moments, measured in score (points). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures employee sentiment at specific journey moments - onboarding, promotion, exit, tools, transfers - rather than as an annual average. Journey-level data matters because experience problems cluster at handoffs and moments of truth, not evenly across the year. Watch for survey fatigue and for scores inflated by favorable-respondent selection in journeys measured only at voluntary checkpoints. Read with regretted attrition by tenure and time loss to bureaucracy.

## Formula

```
EXJB = Average Satisfaction across Key Employee Journey Moments
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** organization
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** culture_employee_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1355 (batch 5)
