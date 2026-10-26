# dea:metric-attrition-cost

Candidate Performance Metric record for **Attrition Cost** (AC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attrition-cost`
- **Name:** Attrition Cost
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AC

## 2. Definition

A Human Resources indicator, Attrition Cost (AC) quantifies exposure to adverse outcomes. Its calculation is Sum of Separation, Replacement, and Productivity Loss Costs, measured in currency value. It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the total cost of employee turnover including separation, replacement, and lost productivity. It matters because it converts turnover from an abstract rate into a budget-line the business respects. Estimates can be deflated by ignoring hidden costs like knowledge loss and team disruption. Read with Employee Turnover Rate and Time to Productivity to test whether modeled costs match observed disruption.

## Formula

```
Sum of Separation, Replacement, and Productivity Loss Costs
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 149 (batch 1)
