# dea:metric-psychological-withdrawal-rate

Candidate Performance Metric record for **Psychological Withdrawal Rate** (PWR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-psychological-withdrawal-rate`
- **Name:** Psychological Withdrawal Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PWR-E

## 2. Definition

Within Culture & Employee Experience, Psychological Withdrawal Rate (PWR-E) is used to gauge exposure to adverse outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Employees below Engagement Threshold with Presenteeism / Employees; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Estimates the share of employees who are disengaged at work - present but mentally checked out - usually derived from survey clusters plus absence and performance signals. It matters because withdrawal precedes attrition, and quiet disengagement damages customers before anyone resigns. Composite estimates carry real noise, and teams under survey pressure learn to mask. Read with engagement trends, regretted attrition, and internal trust score.

## Formula

```
Employees below Engagement Threshold with Presenteeism / Employees
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** culture_employee_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1363 (batch 5)
