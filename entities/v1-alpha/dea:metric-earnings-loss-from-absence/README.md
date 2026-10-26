# dea:metric-earnings-loss-from-absence

Candidate Performance Metric record for **Earnings Loss from Absence** (ELA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-earnings-loss-from-absence`
- **Name:** Earnings Loss from Absence
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ELA

## 2. Definition

A Employee Wellbeing indicator, Earnings Loss from Absence (ELA) quantifies exposure to adverse outcomes. Its calculation is Absence Days x Average Daily Output Value, measured in currency value. It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Earnings loss from absence measures the financial impact of missed work - direct absence cost plus coverage and productivity effects - and it is the translation metric that converts absence statistics into the language of management: percentages become currency. Its construction requires honest assumptions about replacement cost (agency or temporary cover costs materially more than the absent employee's wage), productivity spillover (colleagues absorbing work lose their own output), and service effects (missed revenue when work goes undone). The decomposition by absence category is the management information: short-term intermittent absence (which carries the highest management-intervention potential), long-term absence (which dominates cost), and certified versus uncertified. Read with absence rate and duration distribution as the raw material, intervention-program ROI evidence, and the productivity-impact estimate quality which is usually the weakest link in the calculation.

## Formula

```
ELA = Absence Days x Average Daily Output Value
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1234 (batch 4)
