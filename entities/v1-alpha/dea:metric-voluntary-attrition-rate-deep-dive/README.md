# dea:metric-voluntary-attrition-rate-deep-dive

Candidate Performance Metric record for **Voluntary Attrition Rate (Deep Dive)** (VARRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-voluntary-attrition-rate-deep-dive`
- **Name:** Voluntary Attrition Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VARRDD

## 2. Definition

Voluntary Attrition Rate (Deep Dive) (VARRDD) addresses the retention of customers, users, or assets over time and is a fixture of employee engagement & culture (deep dive) reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Voluntary Leavers / Average Headcount, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures employees choosing to leave as a share of headcount. Voluntary attrition is the controllable half of turnover. Definitions that quietly exclude internal transfers and returns distort comparisons. Read with regretted attrition ratio and critical talent retention rate (Deep Dive).

## Formula

```
Voluntary Leavers / Average Headcount
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** retention
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3860 (batch 8)
