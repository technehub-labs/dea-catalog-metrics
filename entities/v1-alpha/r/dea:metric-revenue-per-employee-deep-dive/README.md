# dea:metric-revenue-per-employee-deep-dive

Candidate Performance Metric record for **Revenue per Employee (Deep Dive)** (RPE-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-employee-deep-dive`
- **Name:** Revenue per Employee (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPE-D

## 2. Definition

Revenue per Employee (Deep Dive) (RPE-D) captures how efficiently resources are converted into outputs for organizations tracking balanced scorecard - financial perspective. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Revenue / Average Employees, expressed in currency per unit. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures revenue generated per headcount. It is the crudest but most comparable productivity number at company level. It penalizes strategically necessary heavy hiring phases and rewards under-hiring decay. Read with operating margin trend and human capital ROI.

## Formula

```
RPE-D = Revenue / Average Employees
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** strategy
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_financial_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3055 (batch 7)
