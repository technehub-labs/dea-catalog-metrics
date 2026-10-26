# dea:metric-attrition-cost-impact

Candidate Performance Metric record for **Attrition Cost Impact** (ACI-WF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attrition-cost-impact`
- **Name:** Attrition Cost Impact
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACI-WF

## 2. Definition

Within Workforce Planning & Productivity, Attrition Cost Impact (ACI-WF) is used to gauge the economic value created or preserved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Replacement and Productivity Cost per Regretted Leaver, measured in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the full financial impact of turnover: recruiting, lost productivity, onboarding, and knowledge loss. Cost converts attrition from HR statistic to P&L issue. Models using only replacement recruiting cost understate by half or more. Read with attrition cost per departure and regretted attrition ratio.

## Formula

```
Replacement and Productivity Cost per Regretted Leaver
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3910 (batch 8)
