# dea:metric-training-hours-per-employee

Candidate Performance Metric record for **Training Hours per Employee** (THPE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-training-hours-per-employee`
- **Name:** Training Hours per Employee
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** THPE

## 2. Definition

Training Hours per Employee (THPE) addresses the utilization or availability of capacity and is a fixture of human resources reporting. It is defined as Total Training Hours / Average Headcount; the result is stated in hours. It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures average training hours delivered per employee. It matters as the input measure for capability building, though only outcomes matter in the end. Gaming risk includes counting mandatory compliance click-throughs as development hours. Read with Training ROI and Internal Fill Rate to confirm hours translate into skills the organization actually uses.

## Formula

```
Total Training Hours / Average Headcount
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 139 (batch 1)
