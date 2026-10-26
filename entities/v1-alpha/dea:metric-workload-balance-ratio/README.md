# dea:metric-workload-balance-ratio

Candidate Performance Metric record for **Workload Balance Ratio** (WBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workload-balance-ratio`
- **Name:** Workload Balance Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WBR

## 2. Definition

Workload Balance Ratio (WBR) measures exposure to adverse outcomes in the Employee Wellbeing domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Employees above Sustainable Workload Threshold / Total Employees, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the distribution of workload across team members. It matters because chronic imbalance drives burnout, quiet quitting, and single-point failure. Balance measured by task count can hide severity and cognitive-load skew. Read with Overtime Hours distribution and Absence Rate to confirm balance is real where it matters.

## Formula

```
Employees above Sustainable Workload Threshold / Total Employees
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** employee_wellbeing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1237 (batch 4)
