# dea:metric-regretted-attrition-ratio

Candidate Performance Metric record for **Regretted Attrition Ratio** (RAR-EE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regretted-attrition-ratio`
- **Name:** Regretted Attrition Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RAR-EE

## 2. Definition

Within Employee Engagement & Culture (Deep Dive), Regretted Attrition Ratio (RAR-EE) is used to gauge the retention of customers, users, or assets over time. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Regretted Leavers / Total Leavers, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of departures the organization genuinely regrets losing. Regretted attrition isolates the losses that damage capability from the healthy sorting of turnover. Regret classifications set by exiting managers drift toward none-regretted. Read with high performer retention rate and voluntary attrition rate (Deep Dive).

## Formula

```
Regretted Leavers / Total Leavers
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3861 (batch 8)
