# dea:metric-burnout-risk-index

Candidate Performance Metric record for **Burnout Risk Index** (BRI-EE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-burnout-risk-index`
- **Name:** Burnout Risk Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BRI-EE

## 2. Definition

Burnout Risk Index (BRI-EE) captures exposure to adverse outcomes for organizations tracking employee engagement & culture (deep dive). It is computed as Composite of Workload, Recovery and Exhaustion Indicators, expressed in index (0-100 or normalized). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the composite leading indicators of burnout across teams (sustained overtime, workload spikes, recovery deficit). Burnout converts into attrition, errors, and absence after a lag. Indexes that only measure self-reported exhaustion arrive post-fact. Read with overtime utilization rate and employee assistance program utilization.

## Formula

```
BRI-EE = Composite of Workload, Recovery and Exhaustion Indicators
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** employee_engagement_culture_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3870 (batch 8)
