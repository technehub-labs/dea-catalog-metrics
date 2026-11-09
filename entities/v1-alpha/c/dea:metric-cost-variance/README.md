# dea:metric-cost-variance

Candidate Performance Metric record for **Cost Variance** (CV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-variance`
- **Name:** Cost Variance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CV

## 2. Definition

Cost Variance (CV) measures conformance to standards, plans, or obligations in the Project Management domain. It is defined as Earned Value - Actual Cost; the result is stated in currency value. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

CV is earned value minus actual cost - the gap between the budgeted worth of work performed and what it really cost. Negative means over budget on the work performed so far, independent of how far along the project is. Unlike percent-spent comparisons, CV is comparable across projects and periods, and under EVM assumptions the final overrun is often near the current cumulative CV unless efficiency changes. It is the base number behind CPI (CV divided by earned value) and is most useful in trend form.

## Formula

```
CV = Earned Value - Actual Cost
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** transformation
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Earned Value Management (DoD/NASA tradition)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 351 (batch 1)
